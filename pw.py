import scrapy


class PwSpider(scrapy.Spider):
    name = 'pw'
    allowed_domains = ['primewire.mx']
    start_urls = ['http://primewire.mx/']

    def parse(self, response):
        pass
