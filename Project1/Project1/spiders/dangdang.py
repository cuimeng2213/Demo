from scrapy import Spider
from scrapy.http import Request
from Project1.items import Project1Item



class DDangSpider(Spider):
	name = 'dd'
	allowed_hosts = ['dangdang.com','category.dangdang.com']
	start_urls = ['http://category.dangdang.com/pg1-cp01.54.06.00.00.00.html']

	def parse(self, response):
		item = Project1Item()
		item['title'] = response.xpath('//p[@class="name"]/a/@title').extract()
		item['link'] = response.xpath('//p[@class="name"]/a/@href').extract()
		item['comment'] = response.xpath('//a[@class="search_comment_num"]/text()').extract()
		next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
#        print('AAAAAA: title', item['title'])
#        print('AAAAAA: link', item['link'])
#        print('AAAAAA: comment', item['comment'])
		print('AAAAAA: next', next_page)
		yield item

		if next_page:
			url = 'http://category.dangdang.com'+next_page
			yield Request(url,callback=self.parse)
	

