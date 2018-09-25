# -*- coding: utf-8 -*-
import scrapy


class UavSpider(scrapy.Spider):
    name = 'uav'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def parse(self, response):
        pass
