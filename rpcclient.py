import xmlrpclib
s = xmlrpclib.ServerProxy('http://localhost:8000')
p = int(input("Integer: "))
if p<=0:
    print "Error"
else:
 print s.myfunction(p)
