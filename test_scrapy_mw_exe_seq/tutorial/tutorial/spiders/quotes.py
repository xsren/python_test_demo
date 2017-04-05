# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # allowed_domains = ["quotes.toscrape.com"]
    # start_urls = ['http://quotes.toscrape.com/']

    def start_requests(self):
        urls = [
            # 'http://quotes.toscrape.com/page/1/',
            # 'http://quotes.toscrape.com/page/2/',
            # 'http://www.baidu.com',
            # 'http://0.0.0.0:5000/',
        ]
        for i in xrange(3):
            urls.append('http://0.0.0.0:5000/?a=%s'%i)
        for url in urls:
            yield scrapy.Request(url=url, 
                                callback=self.parse, 
                                )

    def parse(self, response):
        # import pdb
        # pdb.set_trace()
        
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)