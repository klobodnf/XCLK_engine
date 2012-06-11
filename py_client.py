#!/usr/bin/env python

import sys
import decimal
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

cpu_ratio = str(cpu_status_2.cpu_status())
ssi.cupRatio = decimal.Decimal(cpu_ratio).quantize(decimal.Decimal('0.01'))

ssi.memTotal = memory_status._get_mem_usage()[0]
ssi.memUsed =  memory_status._get_mem_usage()[1]

memory_ratio = str(memory_status._get_mem_usage()[2])
ssi.memRatio = decimal.Decimal(memory_ratio).quantize(decimal.Decimal('0.01'))

ssi.diskTotal = hd_status.disk_stat()[0]
ssi.diskUsed = hd_status.disk_stat()[1]

disk_ratio = str(hd_status.disk_stat()[2])
ssi.diskRatio = decimal.Decimal(disk_ratio).quantize(decimal.Decimal('0.01'))

net_delay = str(net_status.get_net_stat(URL))
ssi.netDelay = decimal.Decimal(net_delay).quantize(decimal.Decimal('0.01'))

send_state_info(ssi, SERVER_IP, SERVER_PORT)
