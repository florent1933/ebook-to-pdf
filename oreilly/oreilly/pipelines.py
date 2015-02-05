# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class OreillyPipeline(object):
    def process_item(self, item, spider):
    	if not item['author'] and not item['title']:
    		raise DropItem("Missing author or title in %s" % item)

    	with open( item['title']+ '.txt', 'a') as f:
  			f.write( item['content'])

        return item
