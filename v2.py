#coding: utf-8
from lxml import etree
import requests
import urllib
import time

"""
显示图片下载进度
"""
def Schedule(blocknum, blocksize, totalsize):
	print('{}{}{}'.format(blocknum,blocksize,totalsize))
	per = 100 * blocknum*blocksize / totalsize
	if per > 100:
		per = 100
	print('recv: {}'.format(per))

base_url='http://www.ivsky.com/tupian/dongwutupian/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0'

headers = {
	'User-Agent':user_agent,
}
oldUrl = set()
newUrl = set()
newUrl.add(base_url)

while True:
	realUrl = newUrl.difference(oldUrl).pop()
	oldUrl.add(realUrl)
	print(realUrl)
	r = requests.get(realUrl)
	html = etree.HTML(r.text)
	newUrls = html.xpath('/html/body/div[3]/div[2]/div[5]/a')
	time.sleep(0.5)
	for a in newUrls:
		url = a.xpath('./@href')[0]
		if not url.startswith('http'):
			url = 'http://www.ivsky.com'+url
		newUrl.add(url)
	
	if html is None:
		print('is none')
	imgs = html.xpath('.//img/@src')

	for img in imgs:
		name = img.split('/')[-1]
		print(img)
		urllib.request.urlretrieve(img,'./images/'+name,Schedule)
		time.sleep(0.5)



