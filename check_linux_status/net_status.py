#!/usr/bin/env python
import os, re

url = 'weibo.com'
local_url = '127.0.0.1'
invalue_url = 'www.facebook.com'

## example:
##64 bytes from 180.149.134.17: icmp_seq=1 ttl=53 time=37.4 ms

re_ping_parser = re.compile(r'.*icmp_seq=(?P<icmp>\d*).*ttl=(?P<ttl>\d*).*time=(?P<time>\d*[.]\d*|\d*)\s*ms')

def get_net_stat(url):
	lines = os.popen('ping ' + url + ' -w 1').readlines()
	
	## if not found the icmp_seq, that's because the url is broken.
	if lines[1].find('icmp_seq') == -1:
		return 0.0
	else:
		match=re_ping_parser.match(lines[1])
		icmp,ttl,time=match.groups(['icmp', 'ttl', 'time'])

		#print icmp
		#print ttl
		return float(time)
