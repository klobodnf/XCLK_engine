#!/usr/bin/env python
import os

def disk_stat():
	hd={}
	disk = os.statvfs("/")
	hd['available'] = disk.f_bsize * disk.f_bavail
	hd['capacity'] = disk.f_bsize * disk.f_blocks
	hd['used'] = disk.f_bsize * disk.f_bfree
	return hd

print disk_stat()
