# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UavItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    brand = scrapy.Field()
    name = scrapy.Field()
    id_ = scrapy.Field()
    shop = scrapy.Field()
    weight = scrapy.Field()
    place = scrapy.Field()
    
