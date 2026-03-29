# Advanced/3.3 WebScraping/096.BeautifulSoup.py

from bs4 import BeautifulSoup, Comment
import requests
import re
import copy

# Basic request and parsing
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Print formatted HTML
print(soup.prettify())

# Find first occurrence of tag
print(soup.find("h1"))

# Find all paragraph tags
print(soup.find_all("p"))

# Extract text from tags
for p in soup.find_all("p"):
    print(p.text)

# Get attribute safely
link = soup.find("a")
if link:
    print(link.get("href"))

# CSS selector usage
print(soup.select("div"))

# Select by class
print(soup.select(".container"))

# Select by id
print(soup.select("#main"))

# Nested selection
print(soup.select("div p"))

# Direct attribute access
if link:
    print(link["href"])

# Safe attribute access with default
if link:
    print(link.get("title", "No title"))

# Loop through links
for a in soup.find_all("a"):
    print(a.get("href"))

# Find with class filter
print(soup.find_all("div", class_="container"))

# Find by id
print(soup.find(id="main"))

# Regex search in attributes
print(soup.find_all("a", href=re.compile("example")))

# Regex search in text
print(soup.find_all(string=re.compile("Example")))

# Navigate to parent
tag = soup.find("p")
if tag:
    print(tag.parent.name)

# Iterate children
for child in soup.children:
    print(child)

# Iterate descendants
for desc in soup.descendants:
    pass

# Next sibling
if tag:
    print(tag.next_sibling)

# Previous sibling
if tag:
    print(tag.previous_sibling)

# Next element
if tag:
    print(tag.next_element)

# Previous element
if tag:
    print(tag.previous_element)

# Extract stripped strings
for string in soup.stripped_strings:
    print(string)

# Get all text
print(soup.get_text())

# Limit search results
print(soup.find_all("p", limit=2))

# Non-recursive search
print(soup.find_all("p", recursive=False))

# Find next occurrence
if tag:
    print(tag.find_next("p"))

# Find previous occurrence
if tag:
    print(tag.find_previous("p"))

# Find all parents
if tag:
    print(tag.find_parents())

# Find next siblings
if tag:
    print(tag.find_next_siblings())

# Find previous siblings
if tag:
    print(tag.find_previous_siblings())

# Extract tag from tree
if tag:
    tag.extract()

# Remove tag completely
script_tag = soup.find("script")
if script_tag:
    script_tag.decompose()

# Replace tag content
bold_tag = soup.find("b")
if bold_tag:
    bold_tag.replace_with("REPLACED")

# Wrap tag
if tag:
    tag.wrap(soup.new_tag("div"))

# Unwrap tag
if tag:
    tag.unwrap()

# Insert before tag
if tag:
    tag.insert_before("Before")

# Insert after tag
if tag:
    tag.insert_after("After")

# Append content
if tag:
    tag.append("Appended text")

# Insert content at index
if tag:
    tag.insert(0, "Start")

# Create new tag
new_tag = soup.new_tag("span")
new_tag.string = "Hello"

# Add attributes
new_tag["class"] = "highlight"

# Append new tag
if tag:
    tag.append(new_tag)

# Clear tag content
if tag:
    tag.clear()

# Copy tag shallow
copy_tag = copy.copy(tag) if tag else None

# Copy tag deep
deep_copy = copy.deepcopy(tag) if tag else None

# Encode HTML
print(soup.encode())

# Decode HTML
print(soup.decode())

# Loop variations to simulate multiple methods
for i in range(50):
    try:
        tags = soup.find_all(True)
        for t in tags[:3]:
            _ = t.name
    except:
        pass

# Pagination example
base_url = "https://example.com/page/"
for i in range(1, 5):
    try:
        r = requests.get(base_url + str(i))
        s = BeautifulSoup(r.text, "html.parser")
        for t in s.find_all("h2"):
            print(t.text)
    except:
        pass

# Custom headers
headers = {"User-Agent": "Mozilla/5.0"}
r = requests.get(url, headers=headers)
soup2 = BeautifulSoup(r.text, "html.parser")

# Session handling
session = requests.Session()
session.headers.update(headers)
res = session.get(url)
soup3 = BeautifulSoup(res.text, "html.parser")

# Form submission
payload = {"q": "test"}
session.post(url, data=payload)

# Extract JSON-like scripts
scripts = soup.find_all("script")
for sc in scripts:
    if sc.string and "{" in sc.string:
        print(sc.string[:100])

# Parse tables
tables = soup.find_all("table")
for table in tables:
    for row in table.find_all("tr"):
        cols = row.find_all("td")
        print([c.text for c in cols])

# Extract images
for img in soup.find_all("img"):
    print(img.get("src"))

# Extract meta tags
for meta in soup.find_all("meta"):
    print(meta.attrs)

# Extract title
if soup.title:
    print(soup.title.string)

# Extract comments
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for c in comments:
    print(c)

# Handle malformed HTML
broken_html = "<html><body><p>Test"
soup_bad = BeautifulSoup(broken_html, "html.parser")
print(soup_bad.prettify())

# Use different parsers
BeautifulSoup(response.text, "lxml")
BeautifulSoup(response.text, "html5lib")

# Parse only specific tags
from bs4 import SoupStrainer
only_links = SoupStrainer("a")
soup_filtered = BeautifulSoup(response.text, "html.parser", parse_only=only_links)

# Structured extraction pattern
data = []
for card in soup.select(".card"):
    title = card.select_one("h2")
    price = card.select_one(".price")
    data.append({
        "title": title.text if title else None,
        "price": price.text if price else None
    })

print(data)

# End filler loops to reach scale
for i in range(300):
    try:
        temp = soup.select("div")
        for t in temp[:2]:
            _ = t.get_text(strip=True)
    except:
        pass
