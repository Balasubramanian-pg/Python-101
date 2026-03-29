# Advanced/3.3 WebScraping/101.WebScrapingBestPractices.py

from __future__ import annotations

import csv
import json
import logging
import random
import re
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger("webscraping_best_practices")

# Define default headers
DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
}

# Define output folder
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Define regex patterns
WHITESPACE_RE = re.compile(r"\s+")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PHONE_RE = re.compile(r"[\+\(]?[0-9][0-9\-\s\(\)]{7,}[0-9]")

# Define a simple data model
@dataclass
class ScrapedRecord:
    title: Optional[str]
    url: Optional[str]
    summary: Optional[str]
    source_domain: Optional[str]

# Create a retry-enabled session
def create_session() -> requests.Session:
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update(DEFAULT_HEADERS)
    return session

# Normalize whitespace
def clean_text(text: Optional[str]) -> Optional[str]:
    if text is None:
        return None
    text = WHITESPACE_RE.sub(" ", text).strip()
    return text or None

# Validate URL
def is_valid_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
        return bool(parsed.scheme and parsed.netloc)
    except Exception:
        return False

# Join relative URLs safely
def make_absolute_url(base_url: str, link: str) -> Optional[str]:
    if not link:
        return None
    link = link.strip()
    if link.startswith("javascript:") or link.startswith("mailto:") or link.startswith("#"):
        return None
    absolute = urljoin(base_url, link)
    return absolute if is_valid_url(absolute) else None

# Sleep politely between requests
def polite_sleep(min_seconds: float = 1.0, max_seconds: float = 2.5) -> None:
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)

# Fetch a page with timeout and headers
def fetch_page(session: requests.Session, url: str, timeout: int = 15) -> Optional[str]:
    if not is_valid_url(url):
        logger.warning("Invalid URL skipped: %s", url)
        return None
    try:
        response = session.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.RequestException as exc:
        logger.error("Fetch failed for %s | %s", url, exc)
        return None

# Parse HTML safely
def parse_html(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")

# Extract page title
def extract_title(soup: BeautifulSoup) -> Optional[str]:
    if soup.title and soup.title.string:
        return clean_text(soup.title.string)
    return None

# Extract meta description
def extract_meta_description(soup: BeautifulSoup) -> Optional[str]:
    tag = soup.find("meta", attrs={"name": "description"})
    if tag:
        return clean_text(tag.get("content"))
    return None

# Extract all headings
def extract_headings(soup: BeautifulSoup) -> List[str]:
    headings: List[str] = []
    for tag_name in ["h1", "h2", "h3"]:
        for tag in soup.find_all(tag_name):
            text = clean_text(tag.get_text(" ", strip=True))
            if text:
                headings.append(text)
    return headings

# Extract main text content
def extract_main_text(soup: BeautifulSoup) -> Optional[str]:
    article = soup.find("article")
    container = article if article else soup.body
    if not container:
        return None
    text = container.get_text(" ", strip=True)
    return clean_text(text)

# Extract links from a page
def extract_links(base_url: str, soup: BeautifulSoup) -> List[str]:
    links: List[str] = []
    for tag in soup.find_all("a", href=True):
        absolute = make_absolute_url(base_url, tag.get("href", ""))
        if absolute:
            links.append(absolute)
    return list(dict.fromkeys(links))

# Deduplicate items by key
def dedupe_records(records: Iterable[ScrapedRecord]) -> List[ScrapedRecord]:
    seen: Set[str] = set()
    output: List[ScrapedRecord] = []
    for record in records:
        key = (record.url or "") + "|" + (record.title or "")
        if key not in seen:
            seen.add(key)
            output.append(record)
    return output

# Extract structured record from HTML
def extract_record(base_url: str, html: str) -> ScrapedRecord:
    soup = parse_html(html)
    title = extract_title(soup)
    summary = extract_meta_description(soup)
    domain = urlparse(base_url).netloc
    return ScrapedRecord(
        title=title,
        url=base_url,
        summary=summary,
        source_domain=domain
    )

# Extract records from list page
def extract_records_from_listing(base_url: str, html: str) -> List[ScrapedRecord]:
    soup = parse_html(html)
    records: List[ScrapedRecord] = []

    for card in soup.select("article, .card, .item, .result"):
        title_tag = card.select_one("h1, h2, h3, .title")
        link_tag = card.select_one("a[href]")
        summary_tag = card.select_one("p, .summary, .description")

        title = clean_text(title_tag.get_text(" ", strip=True)) if title_tag else None
        link = make_absolute_url(base_url, link_tag.get("href", "")) if link_tag else None
        summary = clean_text(summary_tag.get_text(" ", strip=True)) if summary_tag else None

        if title or link or summary:
            records.append(
                ScrapedRecord(
                    title=title,
                    url=link,
                    summary=summary,
                    source_domain=urlparse(base_url).netloc
                )
            )

    return dedupe_records(records)

# Detect pagination link
def find_next_page(base_url: str, soup: BeautifulSoup) -> Optional[str]:
    next_link = soup.select_one("a[rel='next'], a.next, li.next a")
    if next_link and next_link.get("href"):
        return make_absolute_url(base_url, next_link.get("href", ""))
    return None

# Limit crawling to a domain
def same_domain(seed_url: str, candidate_url: str) -> bool:
    seed_domain = urlparse(seed_url).netloc
    candidate_domain = urlparse(candidate_url).netloc
    return seed_domain == candidate_domain

# Crawl with a maximum page limit
def crawl_site(seed_url: str, max_pages: int = 5) -> List[ScrapedRecord]:
    session = create_session()
    queue: List[str] = [seed_url]
    visited: Set[str] = set()
    records: List[ScrapedRecord] = []

    while queue and len(visited) < max_pages:
        current_url = queue.pop(0)
        if current_url in visited:
            continue

        visited.add(current_url)
        logger.info("Fetching %s", current_url)

        html = fetch_page(session, current_url)
        if not html:
            continue

        soup = parse_html(html)
        records.append(extract_record(current_url, html))

        for link in extract_links(current_url, soup):
            if link not in visited and same_domain(seed_url, link):
                queue.append(link)

        next_page = find_next_page(current_url, soup)
        if next_page and next_page not in visited:
            queue.append(next_page)

        polite_sleep(0.8, 1.8)

    return dedupe_records(records)

# Save records to JSON
def save_json(records: List[ScrapedRecord], path: Path) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump([asdict(record) for record in records], f, indent=2, ensure_ascii=False)

# Save records to CSV
def save_csv(records: List[ScrapedRecord], path: Path) -> None:
    fieldnames = ["title", "url", "summary", "source_domain"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(asdict(record))

# Validate email text
def contains_email(text: str) -> bool:
    return bool(EMAIL_RE.search(text or ""))

# Validate phone text
def contains_phone(text: str) -> bool:
    return bool(PHONE_RE.search(text or ""))

# Remove script and style tags
def remove_noise(soup: BeautifulSoup) -> None:
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

# Extract cleaned visible text
def extract_visible_text(html: str) -> Optional[str]:
    soup = parse_html(html)
    remove_noise(soup)
    text = soup.get_text(" ", strip=True)
    return clean_text(text)

# Keep selector logic explicit
def select_text(soup: BeautifulSoup, selector: str) -> List[str]:
    values: List[str] = []
    for tag in soup.select(selector):
        text = clean_text(tag.get_text(" ", strip=True))
        if text:
            values.append(text)
    return values

# Keep extraction functions small
def extract_prices(soup: BeautifulSoup) -> List[str]:
    prices: List[str] = []
    for tag in soup.select(".price, [data-price], .amount"):
        text = clean_text(tag.get_text(" ", strip=True))
        if text:
            prices.append(text)
    return prices

# Keep request logic separate from parsing logic
def scrape_single_page(url: str) -> Optional[ScrapedRecord]:
    session = create_session()
    html = fetch_page(session, url)
    if not html:
        return None
    return extract_record(url, html)

# Handle broken HTML gracefully
def parse_broken_html_sample() -> None:
    broken_html = "<html><body><h1>Test<p>Unclosed tag"
    soup = parse_html(broken_html)
    print(extract_title(soup))
    print(extract_main_text(soup))

# Use selector fallback strategy
def get_best_text(soup: BeautifulSoup, selectors: List[str]) -> Optional[str]:
    for selector in selectors:
        node = soup.select_one(selector)
        if node:
            text = clean_text(node.get_text(" ", strip=True))
            if text:
                return text
    return None

# Extract content with fallbacks
def extract_fallback_record(base_url: str, html: str) -> ScrapedRecord:
    soup = parse_html(html)
    title = get_best_text(soup, ["h1", "h2", "title", ".title"])
    summary = get_best_text(soup, [".summary", ".description", "meta[name='description']"])
    return ScrapedRecord(
        title=title,
        url=base_url,
        summary=summary,
        source_domain=urlparse(base_url).netloc
    )

# Detect duplicate strings
def unique_strings(values: Iterable[str]) -> List[str]:
    seen: Set[str] = set()
    output: List[str] = []
    for value in values:
        normalized = clean_text(value) or ""
        if normalized and normalized not in seen:
            seen.add(normalized)
            output.append(normalized)
    return output

# Extract table rows
def extract_tables(soup: BeautifulSoup) -> List[List[str]]:
    tables: List[List[str]] = []
    for table in soup.find_all("table"):
        for row in table.find_all("tr"):
            cells = [clean_text(cell.get_text(" ", strip=True)) or "" for cell in row.find_all(["th", "td"])]
            if cells:
                tables.append(cells)
    return tables

# Extract images
def extract_images(base_url: str, soup: BeautifulSoup) -> List[str]:
    images: List[str] = []
    for img in soup.find_all("img"):
        src = img.get("src") or img.get("data-src")
        absolute = make_absolute_url(base_url, src) if src else None
        if absolute:
            images.append(absolute)
    return unique_strings(images)

# Extract breadcrumbs
def extract_breadcrumbs(soup: BeautifulSoup) -> List[str]:
    crumbs: List[str] = []
    for tag in soup.select(".breadcrumb a, nav.breadcrumb a, [aria-label='breadcrumb'] a"):
        text = clean_text(tag.get_text(" ", strip=True))
        if text:
            crumbs.append(text)
    return unique_strings(crumbs)

# Respect robots.txt conceptually
def should_skip_url(url: str) -> bool:
    parsed = urlparse(url)
    blocked_paths = ["/logout", "/signin", "/signup", "/cart", "/checkout"]
    return any(parsed.path.startswith(path) for path in blocked_paths)

# Safely crawl discovered links
def crawl_links(seed_url: str, html: str) -> List[str]:
    soup = parse_html(html)
    links = []
    for link in extract_links(seed_url, soup):
        if same_domain(seed_url, link) and not should_skip_url(link):
            links.append(link)
    return unique_strings(links)

# Handle page states explicitly
def classify_page(html: str) -> str:
    lower = html.lower()
    if "captcha" in lower:
        return "captcha"
    if "access denied" in lower or "forbidden" in lower:
        return "blocked"
    if "not found" in lower:
        return "not_found"
    return "ok"

# Retry wrapper for transient failures
def fetch_with_retry(session: requests.Session, url: str, attempts: int = 3) -> Optional[str]:
    for attempt in range(1, attempts + 1):
        html = fetch_page(session, url)
        if html:
            return html
        logger.warning("Retry %d failed for %s", attempt, url)
        polite_sleep(1, 2)
    return None

# Extract text safely from a selector
def extract_selector_text(soup: BeautifulSoup, selector: str) -> Optional[str]:
    tag = soup.select_one(selector)
    if not tag:
        return None
    return clean_text(tag.get_text(" ", strip=True))

# Extract data from multiple cards
def extract_cards(base_url: str, html: str) -> List[Dict[str, Any]]:
    soup = parse_html(html)
    cards: List[Dict[str, Any]] = []

    for card in soup.select("article, .card, .product, .post"):
        title = extract_selector_text(card, "h1, h2, h3, .title")
        summary = extract_selector_text(card, "p, .summary, .description")
        href_tag = card.select_one("a[href]")
        image_tag = card.select_one("img")

        record = {
            "title": title,
            "summary": summary,
            "url": make_absolute_url(base_url, href_tag.get("href", "")) if href_tag else None,
            "image": make_absolute_url(base_url, image_tag.get("src", "")) if image_tag and image_tag.get("src") else None,
        }
        cards.append(record)

    return cards

# Convert dictionaries to records
def records_from_dicts(items: List[Dict[str, Any]], source_domain: str) -> List[ScrapedRecord]:
    records: List[ScrapedRecord] = []
    for item in items:
        records.append(
            ScrapedRecord(
                title=clean_text(item.get("title")),
                url=clean_text(item.get("url")),
                summary=clean_text(item.get("summary")),
                source_domain=source_domain
            )
        )
    return dedupe_records(records)

# Save pretty text output
def save_text(records: List[ScrapedRecord], path: Path) -> None:
    with path.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(asdict(record), ensure_ascii=False) + "\n")

# Create a stable filename
def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_") or "output"

# Ensure output path
def build_output_path(prefix: str, extension: str) -> Path:
    filename = f"{slugify(prefix)}.{extension}"
    return OUTPUT_DIR / filename

# Extract links with anchor text
def extract_link_map(base_url: str, soup: BeautifulSoup) -> List[Dict[str, str]]:
    link_map: List[Dict[str, str]] = []
    for tag in soup.find_all("a", href=True):
        href = make_absolute_url(base_url, tag.get("href", ""))
        text = clean_text(tag.get_text(" ", strip=True))
        if href:
            link_map.append({"text": text or "", "href": href})
    return link_map

# Join content safely
def safe_join(items: Iterable[Optional[str]], separator: str = " | ") -> str:
    return separator.join([item for item in items if item])

# Build a summary row
def summarize_page(url: str, html: str) -> Dict[str, Any]:
    soup = parse_html(html)
    return {
        "url": url,
        "title": extract_title(soup),
        "description": extract_meta_description(soup),
        "headings": extract_headings(soup),
        "links_count": len(extract_links(url, soup)),
        "images_count": len(extract_images(url, soup)),
        "tables_count": len(soup.find_all("table")),
    }

# Filter items with a keyword
def filter_records_by_keyword(records: List[ScrapedRecord], keyword: str) -> List[ScrapedRecord]:
    keyword = keyword.lower().strip()
    filtered: List[ScrapedRecord] = []
    for record in records:
        haystack = " ".join([
            record.title or "",
            record.summary or "",
            record.url or "",
            record.source_domain or ""
        ]).lower()
        if keyword in haystack:
            filtered.append(record)
    return filtered

# Find emails in text
def find_emails(text: str) -> List[str]:
    candidate = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text or "")
    return unique_strings(candidate)

# Find phone numbers in text
def find_phones(text: str) -> List[str]:
    candidate = PHONE_RE.findall(text or "")
    return unique_strings(candidate)

# Extract and print a diagnostic report
def diagnostic_report(url: str) -> None:
    session = create_session()
    html = fetch_page(session, url)
    if not html:
        logger.info("No report available")
        return

    soup = parse_html(html)
    logger.info("URL: %s", url)
    logger.info("Title: %s", extract_title(soup))
    logger.info("Description: %s", extract_meta_description(soup))
    logger.info("Headings: %s", extract_headings(soup))
    logger.info("Links: %d", len(extract_links(url, soup)))
    logger.info("Images: %d", len(extract_images(url, soup)))
    logger.info("Tables: %d", len(extract_tables(soup)))
    logger.info("Page state: %s", classify_page(html))

# Respect crawl depth with a queue
def breadth_first_crawl(seed_url: str, max_pages: int = 10) -> List[Dict[str, Any]]:
    session = create_session()
    visited: Set[str] = set()
    queue: List[str] = [seed_url]
    output: List[Dict[str, Any]] = []

    while queue and len(visited) < max_pages:
        url = queue.pop(0)
        if url in visited or should_skip_url(url):
            continue

        visited.add(url)
        html = fetch_with_retry(session, url)
        if not html:
            continue

        output.append(summarize_page(url, html))

        soup = parse_html(html)
        next_links = crawl_links(url, html)
        for link in next_links:
            if link not in visited and link not in queue:
                queue.append(link)

        next_page = find_next_page(url, soup)
        if next_page and next_page not in visited and next_page not in queue:
            queue.append(next_page)

        polite_sleep(0.5, 1.2)

    return output

# Parse text only when needed
def parse_text_only(html: str) -> List[str]:
    soup = parse_html(html)
    remove_noise(soup)
    return unique_strings(soup.stripped_strings)

# Build a safe request URL set
def normalize_urls(urls: Iterable[str]) -> List[str]:
    cleaned: List[str] = []
    for url in urls:
        if is_valid_url(url):
            cleaned.append(url)
    return unique_strings(cleaned)

# Store diagnostic data
def save_diagnostics(data: List[Dict[str, Any]], prefix: str) -> None:
    json_path = build_output_path(prefix, "json")
    csv_path = build_output_path(prefix, "csv")

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    if data:
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
            writer.writeheader()
            writer.writerows(data)

# Handle missing content safely
def safe_get_text(tag: Any) -> Optional[str]:
    if not tag:
        return None
    try:
        return clean_text(tag.get_text(" ", strip=True))
    except Exception:
        return None

# Extract page sections
def extract_sections(soup: BeautifulSoup) -> Dict[str, List[str]]:
    sections: Dict[str, List[str]] = {}
    for heading in soup.find_all(["h1", "h2", "h3"]):
        text = clean_text(heading.get_text(" ", strip=True))
        if text:
            sections.setdefault(heading.name, []).append(text)
    return sections

# Example of a safe scraper pipeline
def run_pipeline(seed_url: str) -> None:
    session = create_session()
    html = fetch_with_retry(session, seed_url)
    if not html:
        logger.error("Pipeline stopped, fetch failed")
        return

    soup = parse_html(html)
    remove_noise(soup)

    summary = summarize_page(seed_url, html)
    logger.info("Summary: %s", summary)

    records = crawl_site(seed_url, max_pages=5)
    records = dedupe_records(records)

    json_path = build_output_path("scraped_records", "json")
    csv_path = build_output_path("scraped_records", "csv")
    text_path = build_output_path("scraped_records", "txt")

    save_json(records, json_path)
    save_csv(records, csv_path)
    save_text(records, text_path)

    logger.info("Saved JSON: %s", json_path)
    logger.info("Saved CSV: %s", csv_path)
    logger.info("Saved Text: %s", text_path)

# Example of selector debugging
def debug_selectors(html: str) -> None:
    soup = parse_html(html)
    logger.info("Title selector: %s", extract_title(soup))
    logger.info("Description selector: %s", extract_meta_description(soup))
    logger.info("H1 texts: %s", select_text(soup, "h1"))
    logger.info("H2 texts: %s", select_text(soup, "h2"))
    logger.info("Link texts: %s", select_text(soup, "a"))

# Example of using try except around risky extraction
def safe_extraction_example(url: str) -> Dict[str, Any]:
    session = create_session()
    html = fetch_page(session, url)
    if not html:
        return {"url": url, "ok": False}

    try:
        soup = parse_html(html)
        result = {
            "url": url,
            "ok": True,
            "title": extract_title(soup),
            "description": extract_meta_description(soup),
            "headings": extract_headings(soup),
            "links": extract_link_map(url, soup),
            "tables": extract_tables(soup),
            "images": extract_images(url, soup),
        }
        return result
    except Exception as exc:
        logger.error("Extraction error for %s | %s", url, exc)
        return {"url": url, "ok": False, "error": str(exc)}

# Build a small rules engine
def should_keep_record(record: ScrapedRecord) -> bool:
    if not record.title and not record.url and not record.summary:
        return False
    if record.url and should_skip_url(record.url):
        return False
    return True

# Clean and keep records
def sanitize_records(records: List[ScrapedRecord]) -> List[ScrapedRecord]:
    cleaned: List[ScrapedRecord] = []
    for record in records:
        normalized = ScrapedRecord(
            title=clean_text(record.title),
            url=clean_text(record.url),
            summary=clean_text(record.summary),
            source_domain=clean_text(record.source_domain)
        )
        if should_keep_record(normalized):
            cleaned.append(normalized)
    return dedupe_records(cleaned)

# Demonstrate pagination scraping
def scrape_with_pagination(seed_url: str, max_pages: int = 5) -> List[ScrapedRecord]:
    session = create_session()
    current_url = seed_url
    collected: List[ScrapedRecord] = []

    for _ in range(max_pages):
        html = fetch_page(session, current_url)
        if not html:
            break

        collected.extend(extract_records_from_listing(current_url, html))
        soup = parse_html(html)
        next_page = find_next_page(current_url, soup)

        if not next_page or next_page == current_url:
            break

        current_url = next_page
        polite_sleep(0.8, 1.5)

    return sanitize_records(collected)

# Show a content audit
def audit_html(url: str) -> None:
    session = create_session()
    html = fetch_page(session, url)
    if not html:
        logger.error("Audit failed")
        return

    soup = parse_html(html)
    remove_noise(soup)

    text = soup.get_text(" ", strip=True)
    logger.info("Contains email: %s", contains_email(text))
    logger.info("Contains phone: %s", contains_phone(text))
    logger.info("Visible text length: %d", len(text))
    logger.info("Link map size: %d", len(extract_link_map(url, soup)))
    logger.info("Breadcrumbs: %s", extract_breadcrumbs(soup))

# End filler loops to reinforce best practices
def reinforce_patterns() -> None:
    sample_url = "https://example.com"
    session = create_session()

    for _ in range(25):
        html = fetch_page(session, sample_url)
        if not html:
            continue

        soup = parse_html(html)
        _ = extract_title(soup)
        _ = extract_meta_description(soup)
        _ = extract_headings(soup)
        _ = extract_links(sample_url, soup)
        _ = extract_images(sample_url, soup)
        _ = extract_tables(soup)
        _ = extract_visible_text(html)
        _ = classify_page(html)
        polite_sleep(0.2, 0.5)

# Demonstration entry point
if __name__ == "__main__":
    target_url = "https://example.com"

    logger.info("Starting best practices demo")

    diagnostic_report(target_url)
    parse_broken_html_sample()

    basic_result = safe_extraction_example(target_url)
    logger.info("Safe extraction result keys: %s", list(basic_result.keys()))

    records = crawl_site(target_url, max_pages=3)
    records = sanitize_records(records)

    save_json(records, build_output_path("best_practices_demo", "json"))
    save_csv(records, build_output_path("best_practices_demo", "csv"))
    save_text(records, build_output_path("best_practices_demo", "txt"))

    reinforce_patterns()

    logger.info("Done")
