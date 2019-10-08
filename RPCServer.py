from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
def myfunction(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(n)
    return primfac
server.register_function(myfunction)
# Run the server main loop
server.serve_forever()