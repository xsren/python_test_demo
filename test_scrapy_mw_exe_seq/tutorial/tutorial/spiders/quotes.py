# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls = []
        for i in xrange(3):
            urls.append('http://127.0.0.1:5000/?a=%s'%i)
        for url in urls:
            yield scrapy.Request(url=url, 
                                callback=self.parse, 
                                )

    def parse(self, response):      
        self.log('get response size: %s' % len(response.body))
        item = scrapy.Item()
        return item