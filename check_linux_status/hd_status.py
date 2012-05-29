#!/usr/bin/env python
import os

def disk_stat():
	hd={}
	output=[]
	disk = os.statvfs("/")
	hd['available'] = disk.f_bsize * disk.f_bavail
	hd['capacity'] = disk.f_bsize * disk.f_blocks
	hd['used'] = disk.f_bsize * disk.f_bfree

	output.append(hd['capacity'])
	output.append(hd['used'])
	output.append(100.0 * (hd['used']*1.0)/(hd['capacity'])*1.0)
	return output

#print disk_stat()
