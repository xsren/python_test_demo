# coding:utf8
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import defer, reactor
import txmongo
from twisted.web import xmlrpc


class CrawlerServer(xmlrpc.XMLRPC):
    allowNone = True

    def __init__(self):
        xmlrpc.XMLRPC.__init__(self)
        mongo = txmongo.MongoConnection()
        foo = mongo.foo  # `foo` database
        self.test = foo.test  # `test` collection

    @defer.inlineCallbacks
    def xmlrpc_insert(self, doc):
        result = yield self.test.insert(doc, safe=True)
        defer.returnValue(repr(result))

    @defer.inlineCallbacks
    def xmlrpc_find(self, spec, limit=10):
        result = yield self.test.find(spec, limit=limit)
        defer.returnValue(repr(result))


if __name__ == '__main__':
    root = Resource()
    root.putChild("xmlrpc", CrawlerServer())
    factory = Site(root)
    reactor.listenTCP(8888, factory)
    reactor.run()
