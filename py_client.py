#!/usr/bin/env python

import sys
sys.path.append('gen-py')

from cpuinfo import CpuStat
from cpuinfo.ttypes import *

sys.path.append('check_linux_status')
import cpu_status

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def send_cpuinfo(cpu_usage):
	try:

		# Make socket
		transport = TSocket.TSocket('localhost', 9090)

		# Buffering is critical. Raw sockets are very slow
		transport = TTransport.TBufferedTransport(transport)

		# Wrap in a protocol
		protocol = TBinaryProtocol.TBinaryProtocol(transport)

		# Create a client to use the protocol encoder
		client = CpuStat.Client(protocol)

		# Connect!
		transport.open()

		cpu_info = client.get_cpuinfo(cpu_usage)
		print "cpu_info:" + str(cpu_info)

		transport.close()

	except Thrift.TException, tx:
		print '%s' % (tx.message)


cpu_usage = cpu_status.get_cpu_usage()
send_cpuinfo(cpu_usage)
