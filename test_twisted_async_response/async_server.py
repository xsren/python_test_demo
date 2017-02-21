#coding:utf8
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor,threads
from twisted.web.server import NOT_DONE_YET
import time

class CrawlerServer(Resource):

    def __init__(self):
        pass

    def render_GET(self, request):
        print "start......"
        d = threads.deferToThread(self.test)
        d.addCallback(self.succeeded,request)
        d.addErrback(self.failed,request)
        print "finish......"
        return NOT_DONE_YET

    def succeeded(self, result, request):
        print result,request
        request.write("<html><body>Sorry to keep you waiting.</body></html>")
        request.finish()

    def failed(self, failure, request):
        return failure

    def test(self):
        print 'test'
        time.sleep(15)

if __name__ == '__main__':

    root = Resource()
    root.putChild("crawler", CrawlerServer())
    factory = Site(root)
    reactor.listenTCP(1234, factory)
    reactor.run()