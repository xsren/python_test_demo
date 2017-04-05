# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class TutorialSpiderMiddleware0(object):
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
        print "0"*30

    def response_received(self, response, request, spider):
        print "A"*60


class TutorialSpiderMiddleware1(object):
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
        print "1"*30

    def response_received(self, response, request, spider):
        print "B"*60

class TutorialSpiderMiddleware2(object):
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
        print "2"*30

    def response_received(self, response, request, spider):
        print "C"*60

class TutorialSpiderMiddleware3(object):
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
        print "3"*30

    def response_received(self, response, request, spider):
        print "D"*60
