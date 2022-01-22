import scrapy

class SpiderOne(scrapy.Spider):
	name = 'spiderone'
	start_urls = ['https://zyte.com/blog/']

	def parse(self, response):
		for title in response.css('.oxy-post-title'):
			yield {'title': title.css('::text').get()}
		for next_page in response.css('a.next'):
			yield response.follow(next_page, self.parse)