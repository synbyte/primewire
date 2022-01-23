import scrapy

class PrimeOne(scrapy.Spider):
    name = 'primeone'
    start_urls = 'https://primewire.mx'

    def parse(self, response):
        for title in response.css('.title')