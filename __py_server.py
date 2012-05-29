#!/usr/bin/env python

import sys
sys.path.append('gen-py')

from reportComputerStatus import slaveStatusInfoService
from reportComputerStatus.ttypes import *


from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class SystemInfoHandler:
	def reportStatusInfo(self, info):
		print "cpu_id:" + str(info.id)
		print "cpuRatio:" + str(info.cupRatio)
		print "MemoryTotal:" + str(info.memTotal)
		print "MemoryUsed:" + str(info.memUsed)
		print "MemoryRatio:" + str(info.memRatio)
		print "HD Total:" + str(info.diskTotal)
		print "HD Used:" + str(info.diskUsed)
		print "HD Ratio:" + str(info.diskRatio)
		print "Network Delay:" + str(info.netDelay)



handler = SystemInfoHandler()
processor = slaveStatusInfoService.Processor(handler)
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
