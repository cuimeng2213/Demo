# coding: utf-8
import codecs
class DataOutput(object):
	"""docstring for DataOutput"""
	def __init__(self):
		self.datas = []
	def store_data(self,data):
		self.datas.append(data)
	def out_put_html(self):
		f = codesc.open('bike.html','w',encoding='utf-8')
		f.write('<html><body><table>')
		for d  in self.datas:
			f.write('<tr>')
			f.write('<td>{}</td>'.format(d['url']))
			f.write('<td>{}</td>'.format(d['title']))
			f.write('<td>{}</td>'.format(d['summary']))
			f.write('</tr>')
		f.write('</table></body></html>')
		f.close()




