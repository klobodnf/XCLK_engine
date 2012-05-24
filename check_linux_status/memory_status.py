#!/usr/bin/env python
import re

re_meminfo_parser = re.compile(r'^(?P<key>\S*):\s*(?P<value>\d*)\s*kB')  

def _get_mem_usage():  
	""" 
	get mem used by percent 
	self.result = falot 
	"""  
	result={}  
	try:  
		fd=open('/proc/meminfo', 'r')  
		lines=fd.readlines()  
	finally:  
		if fd:  
			fd.close()  
	for line in lines:  
		match=re_meminfo_parser.match(line)  
		if not match:  
			continue # skip lines that don't parse  
		key, value=match.groups(['key', 'value'])  
		result[key]=int(value)  
	#print "mem :", 100*(result["MemTotal"]-result["MemFree"])/result["MemTotal"]
	print "MemTotal:" + str(result["MemTotal"]) + "\n"
	print "MemFree:" + str(result["MemFree"]) + "\n"
	return 100.0*(result["MemTotal"]-result["MemFree"])/result["MemTotal"]  

print _get_mem_usage()
