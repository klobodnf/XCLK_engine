#!/usr/bin/env python

import sys
sys.path.append('gen-py')

from hello import Hello
from hello.ttypes import *


from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class Klobohyz:
#	def __init__(self):
#		self.log = {}

	def Hello(self):
		print "hello thrift"

	def Asshole(self):
		print "Asshole"



handler = Klobohyz()
processor = Hello.Processor(handler)
transport = TSocket.TServerSocket('localhost', 9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

# You could do one of these for a multithreaded server
#server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
#server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

print 'Starting the server...'
server.serve()
print 'done.'
