import urlmanager
import htmldownload
import htmlparser
import dataoutput

class SpiderMan(object):
	
	def __init__(self):
		"""初始化你每个模块的实例"""
		self.manager = urlmanager.UrlManager()
		self.parse = htmlparser.HtmlParse()
		self.downLoader = htmldownload.HtmlDownLoad()
		self.dataOut = dataoutput.DataOutput()
	def crawl(self, url):
		self.manager.add_new_url(url)
		while self.manager.has_new_url() and self.manager.old_url_size() < 100:
			newUrl = self.manager.get_new_url()
			html = self.downLoader.download(newUrl)
			urls, data = self.parse.parse(newUrl, html)
			self.manager.add_new_urls(urls)
			self.dataOut.store_data(data)
		self.dataOut.out_put_html()

def main():
	sp = SpiderMan()
	sp.crawl('https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB')


if __name__ == '__main__':
	main()		
		