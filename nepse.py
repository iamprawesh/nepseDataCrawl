import scrapy
from scrapy.crawler import CrawlerProcess


class NepseSpider(scrapy.Spider):
    name = 'nepse'
    # start_urls = ['http://quotes.toscrape.com']

    start_urls = ['http://www.nepalstock.com/main/todays_price/index']

    def parse(self, response):
        # self.log(f'Got message from {response.url}')z
        all_row_item = response.css('div#home-contents tr')
        all_item = all_row_item[2:len(all_row_item)-4]

        # file1 = open("myfile.txt", "w")
        # # \n is placed to indicate EOL (End of Line)
        # file1.write(str(all_item))
        # # file1.write(len(quotes))
        # file1.write("len(quotes)")

        # # file1.writelines(L)
        # file1.close()  # to change file access modes
        for index, single in enumerate(all_item):
            item = {
                "id": single.xpath("td[1]/text()").get().strip(),
                "company_name": single.xpath("td[2]/text()").get().strip(),
                "max_price": single.xpath("td[4]/text()").get().strip(),
                "min_price": single.xpath("td[5]/text()").get().strip(),
                "closing_price": single.xpath("td[6]/text()").get().strip(),
                "previous_closing": single.xpath("td[9]/text()").get().strip(),
                "difference": single.xpath("td[10]/text()").get().strip(),


                # "hello 2": single.xpath("//tr/td[2]/text()").get()
                #         'author': quote.css('[itemprop="author"]::text').get(),
                #         "quote": quote.css('.text::text').get(),
                #         "tags": quote.css('.tag::text').getall()
            }
            yield item
        # next_page_url = response.xpath("//*text()='Next'").get()
        next_page_url = response.xpath("//*[@title='Next Page']/@href").get()
        if next_page_url:
            # next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(NepseSpider)
    process.start()
