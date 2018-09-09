# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['item.m.jd.com']
    start_urls = ['https://item.m.jd.com/ware/detail.json?wareId=%d']

    def parse(self, response):
        request = response.text
        print(request)
