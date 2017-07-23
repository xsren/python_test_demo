import xmlrpclib

srv = xmlrpclib.Server("http://localhost:8888/xmlrpc", allow_none=True)
print "insert:", srv.insert({"name": "foobar", "useDateTime": 1})
print "find:", srv.find({"name": "foobar", "useDateTime": 1})
