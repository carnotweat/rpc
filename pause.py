# 3 is gid
import xmlrpclib
s = xmlrpclib.ServerProxy('http://localhost:6800/rpc')
s.aria2.pause('3')
