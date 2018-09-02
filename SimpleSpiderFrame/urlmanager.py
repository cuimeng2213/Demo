# coding: utf-8
'''
Url管理器类
'''
class UrlManager(object):
	"""url manager """
	def __init__(self):
		self.oldUrl = set()
		self.newUrl = set()
	def has_new_url(self):
		return len(self.newUrl) != 0
	def get_new_url(self):
		new_url = self.newUrl.pop()
		self.oldUrl.add(new_url)
		return new_url
	def add_new_url(self, url):
		if url is None:
			return
		if url not in self.newUrl and url not in self.oldUrl:
			self.newUrl.add(url)
	def add_new_urls(self,urls):
		if urls is None:
			return
		for url in urls:
			self.add_new_url(url)
	def new_url_size(self):
		return len(self.newUrl)

	def old_url_size(self):
		return len(self.oldUrl)


		