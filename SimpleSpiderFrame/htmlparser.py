# coding: utf-8
import re
from urllib.parse import urlparse
from urllib.parse import urljoin
from lxml import etree

class HtmlParse(object):
	"""docstring for HtmlParse"""
	def __init__(self):
		pass
	def parse(self,page_url, html_cont):
		if page_url is None or html_cont is None:
			return
		r = etree.HTML(html_cont)
		new_urls = self._get_new_urls(page_url,r)
		new_datas = self._get_new_datas(page_url,r)
		return new_urls, new_datas

	def _get_new_urls(self,page_url, rsp):
		newUrls = set()
		aHref = rsp.xpath('.//*/a')
		for a in aHref:
			href = a.xpath('./@href')[0]
			if href.startswith('javascript'):
				continue
			new_full_url = urljoin(page_url,href)
			newUrls.add(new_full_url)
		return newUrls

	def _get_new_datas(self,page_url, rsp):
		if page_url is None or rsp is None:
			return None
		data = {}
		data['url'] = page_url
		title = rsp.xpath('/html/body/div[4]/div[2]/div/div[2]/dl[1]/dd/h1/text()')
		data['title'] = title
		summary = rsp.xpath('/html/body/div[4]/div[2]/div/div[2]/div[5]/text()')
		data['summary'] = summary
		return data
