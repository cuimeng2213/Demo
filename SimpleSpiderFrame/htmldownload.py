# coding: utf-8
'''
'''
import requests

class HtmlDownLoad(object):
	"""docstring for HtmlDownLoad"""
	def __init__(self):
		pass
	def download(self,url):
		if url is None:
			return None

		user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0'
		headers = {
			'User-Agent':user_agent,
		}

		rsp = requests.get(url,headers=headers)
		if rsp.status_code == 200:
			rsp.encoding = 'utf-8'
			return rsp.text
		else:
			return None

		