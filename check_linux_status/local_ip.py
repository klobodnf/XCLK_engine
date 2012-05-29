#!/usr/bin/env python

import socket, fcntl, struct  

def get_local_ip(ifname = 'eth1'):  
	    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	    inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))  
	    ret = socket.inet_ntoa(inet[20:24])  
	    return ret  
