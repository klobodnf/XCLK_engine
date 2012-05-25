#!/usr/bin/env python

import sys
sys.path.append('gen-py')

from reportComputerStatus import slaveStatusInfoService
from reportComputerStatus.ttypes import *
#
#sys.path.append('check_linux_status')
#import cpu_status

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def send_state_info(state_info, ip = "localhost", port = 9090):
	try:

		# Make socket
		transport = TSocket.TSocket(ip, port)

		# Buffering is critical. Raw sockets are very slow
		transport = TTransport.TBufferedTransport(transport)

		# Wrap in a protocol
		protocol = TBinaryProtocol.TBinaryProtocol(transport)

		# Create a client to use the protocol encoder
		client = slaveStatusInfoService.Client(protocol)

		# Connect!
		transport.open()

		client.reportStatusInfo(state_info)

		transport.close()

	except Thrift.TException, tx:
		print '%s' % (tx.message)



ssi = StatusInfo()
ssi.id = 11
ssi.ip = "8.8.8.8"
ssi.cupRatio = 12.4
ssi.memTotal = 4423424424
ssi.memUsed = 2423424424 
ssi.memRatio = 42.4
ssi.diskTotal = 242424234
ssi.diskUsed = 142424234
ssi.diskRatio = 33.4
ssi.netDelay = 2323


send_state_info(ssi, '10.188.54.45', 7911)
