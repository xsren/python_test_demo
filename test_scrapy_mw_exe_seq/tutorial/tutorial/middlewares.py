# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class TutorialSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.request_scheduled, signal=signals.request_scheduled)
        crawler.signals.connect(s.response_received, signal=signals.response_received)
        return s

    def request_scheduled(self, request, spider):
        print ('SpiderMiddleware request_scheduled')

    def response_received(self, response, request, spider):
        print ('SpiderMiddleware response_received')

    def process_spider_input(self, response, spider):
        print ('SpiderMiddleware process_spider_input')

    def process_spider_output(self, response, result, spider):
        print ('SpiderMiddleware process_spider_output')
        return result

class TutorialDownloadMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def __init__(self):
        self.status = 'start'

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.request_scheduled, signal=signals.request_scheduled)
        crawler.signals.connect(s.response_received, signal=signals.response_received)
        return s

    def request_scheduled(self, request, spider):
        print ('DownloadMiddleware request_scheduled')

    def response_received(self, response, request, spider):
        print ('DownloadMiddleware response_received')

    def process_request(self, request, spider):
        print ('DownloadMiddleware process_request')

    def process_response(self, request, response, spider):
        print ('DownloadMiddleware process_response')
        return response

class TutorialExtension(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.request_scheduled, signal=signals.request_scheduled)
        crawler.signals.connect(s.response_received, signal=signals.response_received)
        return s

    def request_scheduled(self, request, spider):
        print ('Extension request_scheduled')

    def response_received(self, response, request, spider):
        print ('Extension response_received')

class TutorialPIPELINES(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.request_scheduled, signal=signals.request_scheduled)
        crawler.signals.connect(s.response_received, signal=signals.response_received)
        return s

    def request_scheduled(self, request, spider):
        print ('PIPELINES request_scheduled')

    def response_received(self, response, request, spider):
        print ('PIPELINES response_received')

    def process_item(self, item, spider):
        print ('PIPELINES process_item')
        return item