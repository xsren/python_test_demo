#coding:utf8
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class Test(LineReceiver):

    def dataReceived(self, data):
        self.transport.write("<html>Hello, world!</html>")


class TestFactory(Factory):

    def buildProtocol(self, addr):
        return Test()

if __name__ == '__main__':
    port = 8080
    print 'listen on %s' %port
    reactor.listenTCP(port, TestFactory())
    reactor.run()