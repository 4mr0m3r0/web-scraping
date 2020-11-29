import scrapy
from app.items import AppItem


class FirstSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        "http://books.toscrape.com",
    ]

    def parse(self, response):
        print("Response Type >>> ", type(response))
        elements = response.xpath("//article[@class='product_pod']")

        print("Article books count >> ", elements.__len__())
        for element in elements:
            item = AppItem()
            item['title'] = element.xpath('h3/a/@title').extract()
            item['price'] = element.xpath('div[@class="product_price"]/p[@class="price_color"]/text()').extract()
            item['rating'] = element.xpath('p[@class="star-rating"]/@class').extract()
            yield item

        next_page = response.css("ul.pager > li.next > a::attr(href)").extract_first()
        if next_page:
            print("<<< Next Page URL: >>> ", next_page)
            if self.CATALOGUE in next_page:
                full_next_page = '{0}/{1}'.format(self.start_urls[0], next_page)
            else:
                full_next_page = '{0}/{1}/{2}'.format(self.start_urls[0], self.CATALOGUE, next_page)
            print("<<< Full Next Page URL: >>> ", full_next_page)
            yield scrapy.Request(full_next_page, callback=self.parse)

        print('COMPLETED')
        pass

    CATALOGUE = "catalogue"
