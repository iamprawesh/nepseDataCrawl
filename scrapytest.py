import scrapy
from scrapy.crawler import CrawlerProcess


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        # self.log(f'Got message from {response.url}')z
        quotes = response.css('.quote')
        for quote in quotes:
            item = {
                'author': quote.css('[itemprop="author"]::text').get(),
                "quote": quote.css('.text::text').get(),
                "tags": quote.css('.tag::text').getall()
            }
            yield item
        next_page_url = response.css('li.next > a::attr(href)').get()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start()
