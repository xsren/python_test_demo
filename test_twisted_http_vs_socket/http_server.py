#coding:utf8
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web import resource
from twisted.internet import reactor

class Test(resource.Resource):
    def render_POST(self, request):
        return "<html>Hello, world!</html>"

root = Resource()
root.putChild("test", Test())
factory = Site(root)
port = 8081
print 'run server on %s' % port
reactor.listenTCP(port, factory)
reactor.run()