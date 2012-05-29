#!/usr/bin/env python

import sys
sys.path.append('gen-py')

from reportComputerStatus import slaveStatusInfoService
from reportComputerStatus.ttypes import *

sys.path.append('check_linux_status')
import cpu_status_2
import local_ip
import hd_status
import net_status
import memory_status

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol



NET_CARD_id		=	'eth1'
URL				=	'weibo.com'
SERVER_IP		= 	'10.188.54.45'
#SERVER_IP		=	'localhost'
#SERVER_PORT		=	9090
SERVER_PORT		=	7911

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
ssi.id = 1
ssi.ip = local_ip.get_local_ip(NET_CARD_id)
ssi.cupRatio = float(cpu_status_2.cpu_status())
ssi.memTotal = memory_status._get_mem_usage()[0]
ssi.memUsed =  memory_status._get_mem_usage()[1]
ssi.memRatio = memory_status._get_mem_usage()[2]
ssi.diskTotal = hd_status.disk_stat()[0]
ssi.diskUsed = hd_status.disk_stat()[1]
ssi.diskRatio = hd_status.disk_stat()[2]
ssi.netDelay = float(net_status.get_net_stat(URL))

send_state_info(ssi, SERVER_IP, SERVER_PORT)
