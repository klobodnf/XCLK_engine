#!/usr/bin/env python
import os

#struct just_show_statvfs {
#	unsigned long  f_bsize;    /* file system block size */
#	unsigned long  f_frsize;   /* fragment size */
#	fsblkcnt_t     f_blocks;   /* size of fs in f_frsize units */
#	fsblkcnt_t     f_bfree;    /* # free blocks */
#	fsblkcnt_t     f_bavail;   /* # free blocks for non-root */
#	fsfilcnt_t     f_files;    /* # inodes */
#	fsfilcnt_t     f_ffree;    /* # free inodes */
#	fsfilcnt_t     f_favail;   /* # free inodes for non-root */
#	unsigned long  f_fsid;     /* file system ID */
#	unsigned long  f_flag;     /* mount flags */
#	unsigned long  f_namemax;  /* maximum filename length */
#};

UNIT = 1024*1024*1024.0
def disk_stat():
	hd={}
	output=[]
	disk = os.statvfs("/")
	print disk
	hd['available'] = disk.f_bsize * disk.f_bavail
	hd['free'] = disk.f_bsize * disk.f_bfree
	hd['capacity'] = disk.f_bsize * disk.f_blocks
	hd['used'] = hd['capacity'] - hd['available']

	output.append(hd['capacity'] / UNIT)
	output.append(hd['used'] / UNIT)
	output.append(hd['available'] / UNIT)
	output.append(hd['free'] / UNIT)
	output.append(100.0 * (hd['used']*1.0)/(hd['capacity'])*1.0)
	return output

print disk_stat()
