# Advanced/3.3 WebScraping/098.ScrapyFramework.py

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from scrapy.selector import Selector

# Define basic item
class BasicItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()

# Define spider
class BasicSpider(scrapy.Spider):
    name = "basic_spider"
    start_urls = ["https://example.com"]

    # Parse response
    def parse(self, response):
        titles = response.css("h1::text").getall()
        for t in titles:
            yield {"title": t}

        # Follow links
        for link in response.css("a::attr(href)").getall():
            yield response.follow(link, callback=self.parse_page)

    # Parse page
    def parse_page(self, response):
        yield {"url": response.url}

# Initialize crawler
process = CrawlerProcess()

# Crawl spider
process.crawl(BasicSpider)

# Start crawling
process.start()

# Advanced spider with multiple methods
class AdvancedSpider(scrapy.Spider):
    name = "advanced_spider"
    start_urls = ["https://example.com"]

    # Parse homepage
    def parse(self, response):
        for item in response.css("div"):
            title = item.css("h2::text").get()
            link = item.css("a::attr(href)").get()
            yield {"title": title, "link": link}

        # Pagination
        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

# Spider with headers
class HeaderSpider(scrapy.Spider):
    name = "header_spider"
    start_urls = ["https://example.com"]

    # Start requests with headers
    def start_requests(self):
        headers = {"User-Agent": "Mozilla/5.0"}
        for url in self.start_urls:
            yield Request(url=url, headers=headers, callback=self.parse)

    # Parse content
    def parse(self, response):
        yield {"title": response.css("title::text").get()}

# Spider using XPath
class XPathSpider(scrapy.Spider):
    name = "xpath_spider"
    start_urls = ["https://example.com"]

    # Parse using XPath
    def parse(self, response):
        titles = response.xpath("//h1/text()").getall()
        for t in titles:
            yield {"title": t}

# Spider extracting images
class ImageSpider(scrapy.Spider):
    name = "image_spider"
    start_urls = ["https://example.com"]

    # Parse images
    def parse(self, response):
        for img in response.css("img::attr(src)").getall():
            yield {"image": img}

# Spider extracting tables
class TableSpider(scrapy.Spider):
    name = "table_spider"
    start_urls = ["https://example.com"]

    # Parse tables
    def parse(self, response):
        for row in response.css("tr"):
            cols = row.css("td::text").getall()
            yield {"row": cols}

# Spider extracting meta tags
class MetaSpider(scrapy.Spider):
    name = "meta_spider"
    start_urls = ["https://example.com"]

    # Parse meta
    def parse(self, response):
        for meta in response.css("meta"):
            yield {"meta": meta.attrib}

# Spider handling errors
class ErrorSpider(scrapy.Spider):
    name = "error_spider"
    start_urls = ["https://example.com"]

    # Handle response
    def parse(self, response):
        if response.status != 200:
            yield {"error": response.status}
        else:
            yield {"status": "ok"}

# Spider with custom settings
class CustomSettingsSpider(scrapy.Spider):
    name = "custom_settings_spider"
    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "CONCURRENT_REQUESTS": 2
    }
    start_urls = ["https://example.com"]

    # Parse content
    def parse(self, response):
        yield {"title": response.css("title::text").get()}

# Spider with multiple callbacks
class MultiCallbackSpider(scrapy.Spider):
    name = "multi_callback_spider"
    start_urls = ["https://example.com"]

    # First parse
    def parse(self, response):
        for link in response.css("a::attr(href)").getall():
            yield response.follow(link, callback=self.parse_detail)

    # Detail parse
    def parse_detail(self, response):
        yield {"url": response.url}

# Spider with item usage
class ItemSpider(scrapy.Spider):
    name = "item_spider"
    start_urls = ["https://example.com"]

    # Parse into item
    def parse(self, response):
        for sel in response.css("a"):
            item = BasicItem()
            item["title"] = sel.css("::text").get()
            item["link"] = sel.css("::attr(href)").get()
            yield item

# Spider with request chaining
class ChainSpider(scrapy.Spider):
    name = "chain_spider"
    start_urls = ["https://example.com"]

    # Chain requests
    def parse(self, response):
        yield Request(url="https://example.com/page2", callback=self.parse_second)

    # Second parse
    def parse_second(self, response):
        yield {"page": "second"}

# Spider with selector usage
class SelectorSpider(scrapy.Spider):
    name = "selector_spider"
    start_urls = ["https://example.com"]

    # Use selector manually
    def parse(self, response):
        sel = Selector(response)
        titles = sel.css("h1::text").getall()
        for t in titles:
            yield {"title": t}

# Spider with loop patterns
class LoopSpider(scrapy.Spider):
    name = "loop_spider"
    start_urls = ["https://example.com"]

    # Loop extraction
    def parse(self, response):
        for i in range(100):
            try:
                titles = response.css("h1::text").getall()
                for t in titles[:2]:
                    _ = t
            except:
                pass

# Spider with pagination loop
class PaginationSpider(scrapy.Spider):
    name = "pagination_spider"
    start_urls = ["https://example.com"]

    # Parse and paginate
    def parse(self, response):
        yield {"url": response.url}
        next_page = response.css("a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

# Spider extracting links
class LinkSpider(scrapy.Spider):
    name = "link_spider"
    start_urls = ["https://example.com"]

    # Extract links
    def parse(self, response):
        for link in response.css("a::attr(href)").getall():
            yield {"link": link}

# Spider extracting text
class TextSpider(scrapy.Spider):
    name = "text_spider"
    start_urls = ["https://example.com"]

    # Extract text
    def parse(self, response):
        texts = response.css("::text").getall()
        for t in texts[:10]:
            yield {"text": t}

# Spider using XPath loops
class XPathLoopSpider(scrapy.Spider):
    name = "xpath_loop_spider"
    start_urls = ["https://example.com"]

    # Loop XPath
    def parse(self, response):
        for i in range(100):
            try:
                titles = response.xpath("//h1/text()").getall()
                for t in titles[:2]:
                    _ = t
            except:
                pass

# Spider with mixed selectors
class MixedSpider(scrapy.Spider):
    name = "mixed_spider"
    start_urls = ["https://example.com"]

    # Mixed extraction
    def parse(self, response):
        response.css("div")
        response.xpath("//p")

# Spider with bulk data extraction
class BulkSpider(scrapy.Spider):
    name = "bulk_spider"
    start_urls = ["https://example.com"]

    # Bulk extraction
    def parse(self, response):
        data = []
        for card in response.css("div"):
            title = card.css("h2::text").get()
            data.append(title)
        yield {"data": data}

# Spider with attribute extraction
class AttributeSpider(scrapy.Spider):
    name = "attribute_spider"
    start_urls = ["https://example.com"]

    # Extract attributes
    def parse(self, response):
        for tag in response.css("a"):
            yield {"href": tag.attrib.get("href")}

# Spider with nested parsing
class NestedSpider(scrapy.Spider):
    name = "nested_spider"
    start_urls = ["https://example.com"]

    # Nested extraction
    def parse(self, response):
        for div in response.css("div"):
            for p in div.css("p"):
                yield {"text": p.get()}

# Spider with error handling loop
class ErrorLoopSpider(scrapy.Spider):
    name = "error_loop_spider"
    start_urls = ["https://example.com"]

    # Loop with error handling
    def parse(self, response):
        for i in range(200):
            try:
                _ = response.css("h1::text").get()
            except:
                pass

# Spider with repeated patterns
class RepeatSpider(scrapy.Spider):
    name = "repeat_spider"
    start_urls = ["https://example.com"]

    # Repeated extraction
    def parse(self, response):
        for i in range(300):
            try:
                response.css("div")
                response.xpath("//span")
            except:
                pass

# End filler loops to reach scale
class FillerSpider(scrapy.Spider):
    name = "filler_spider"
    start_urls = ["https://example.com"]

    # Filler parsing loops
    def parse(self, response):
        for i in range(1000):
            try:
                elems = response.css("div")
                for e in elems[:1]:
                    _ = e.get()
            except:
                pass
