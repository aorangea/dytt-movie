# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MoviePipeline(object):
    def __init__(self):
        self.sql = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='5408',db='books',charset='utf8')
        self.cursor = self.sql.cursor()

    def process_item(self, item, spider):
        sqll = "insert into movie(title,pic,showtime,dload) values('%s','%s','%s','%s')" % \
               (item['title'],item['pic'],item['showtime'],item['dload'])
        self.cursor.execute(sqll)
        self.sql.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.sql.close()
