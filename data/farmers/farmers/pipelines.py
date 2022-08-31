# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class FarmersPipeline(object):
#     def process_item(self, item, spider):
#         return item

import json
from scrapy.exporters import JsonItemExporter

class FarmersPipeline(object):
#     def open_spider(self, farmers):
#         self.file = open('usda.jl', 'w')
#         # Your scraped items will be saved in the file 'scraped_items.json'.
#         # You can change the filename to whatever you want.
#         self.file.write('{"index":{}}')

   def __init__(self): 
      self.file = open('usda_oip_scl.jl', 'wb')
      self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)       

   def process_item(self, item, spider): 
      line = '{"index":{"_index":"scl_locations","_type":"serviceCenter"}}' + "\n" + json.dumps(dict(item)) + "\n" 
      self.file.write(line) 
      return item