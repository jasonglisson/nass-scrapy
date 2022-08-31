# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class OipCountyPipeline(object):
#     def process_item(self, item, spider):
#         return item

import json
from scrapy.exporters import JsonLinesItemExporter

class OipCountyPipeline(object):
#     def open_spider(self, farmers):
#         self.file = open('usda.jl', 'w')
#         # Your scraped items will be saved in the file 'scraped_items.json'.
#         # You can change the filename to whatever you want.
#         self.file.write('{"index":{}}')

  #  def __init__(self): 
  #     self.file = open('oip_county.jl', 'w+b')
  #     self.exporter = JsonLinesItemExporter(self.file, encoding="utf-8", ensure_ascii=False) 

  #  def process_item(self, item, spider): 
  #     line = '{"index":{ "_index":"oip_county","_type":"serviceCenter"}}' + "\n" + json.dumps(dict(item)) + "\n" 
  #     self.file.write(line) 
  #     return item
  #     self.exporter.finish_exporting()
  #     self.file.close()      

    # def open_spider(self, spider):
    #     self.file = open('oip_county.jl', 'w')

    # def close_spider(self, spider):
    #     self.file.close()

    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item)) + "\n"
    #     self.file.write(line)
    #     return item

  #  def open_spider(self, spider):
  #     self.file = open('oip_county.jl', 'w')
  #     self.exporter = JsonLinesItemExporter(self.file, encoding="utf-8", ensure_ascii=False) 

  #  def process_item(self, item, spider):
  #     line = '{"index":{ "_index":"oip_county","_type":"serviceCenter"}}' + "\n" + json.dumps(dict(item)) + "\n"
  #     self.file.write(line)
  #     return item

  #  def close_spider(self, spider):
  #     self.exporter.finish_exporting()
  #     self.file.close()      

     def __init__(self): 
      self.file = open('oip_county.jl', 'w')
      self.exporter = JsonLinesItemExporter(self.file, encoding="utf-8", ensure_ascii=False) 

     def process_item(self, item, spider): 
      line = '{"index":{ "_index":"oip_county","_type":"serviceCenter"}}' + "\n" + json.dumps(dict(item)) + "\n" 
      self.file.write(line) 
      return item
      self.exporter.finish_exporting()
      self.file.close() 