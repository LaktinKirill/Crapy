import scrapy
import csv

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru/category/divany-i-kresla"]

    def __init__(self, *args, **kwargs):
        super(DivannewparsSpider, self).__init__(*args, **kwargs)
        self.file = open('divans.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.file, fieldnames=['name', 'price', 'url'])
        self.writer.writeheader()

    def parse(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
            item = {
                'name': divan.css('div.lsooF span::text').get(),
                'price': divan.css('div.pY3d2 span::text').get(),
                'url': divan.css('a').attrib['href']
            }
            self.writer.writerow(item)
            yield item

    def closed(self, reason):
        self.file.close()


