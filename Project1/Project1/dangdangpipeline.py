class DangDang(object):
	def __init__(self):
		self.opener = open('data.txt','w')
		self.opener.write('title,link,comment\n')
	def process_item(self, item, spider):
		for i in range(len(item['title'])):
			self.opener.write(item['title'][i]+','+item['link'][i]+','+item['comment'][i]+'\n')

		return item
	def process_close(self):
		print('####################: spider over')
		self.opener.close()
