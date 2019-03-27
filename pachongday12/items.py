# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Pachongday12Item(scrapy.Item):
    # define the fields for your item here like:
    num = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    tv = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
    dy = scrapy.Field()
    zy = scrapy.Field()


