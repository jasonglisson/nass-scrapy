# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NassMigrateItem(scrapy.Item):
    # define the fields for your item here like:
    survey_name = scrapy.Field()
    alt_title = = scrapy.Field()
    referring_url = scrapy.Field()
    banner_image_urls = scrapy.Field()
    body = scrapy.Field()
    pass
