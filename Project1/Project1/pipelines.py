# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Project1Pipeline(object):
    def __init__(self):
        self.opener = open('data.txt','w')
        self.opener.write('title\tlink\tcomment\t\n')
    def process_item(self, item, spider):
#        print('### len: ',len(item), item)
        for i in range(len(item['title'])):
            print(item['title'][i])
            print(item['link'][i])
            print(item['comment'][i])
            self.opener.write(item['title'][i]+'\t'+item['link'][i]+'\t'+item['comment'][i]+'\t\n')
        return item
    def process_close(self):
        self.opener.close()
