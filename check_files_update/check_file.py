#!/usr/bin/env python

import os
import time
DIR = '~/thrift_py_cpustat/test'
CMD = 'ls ' + DIR +' | grep -v .log'

H = 3600
M = 60

SLEEP_TIME = 5

class File:
	def __int__(self, filename = None, filesize = None):
		self.filename = filename
		self.filesize = filesize


list_err_file = []
list_files = [[],[]]

##################################################################################
##################################################################################
##################################################################################

#statinfo = os.stat(r'check_file.py')

#print statinfo


#print "create time:" + str(time.localtime(statinfo.st_ctime))
#print "\n\n"
#print "modified time:" + str(time.localtime(statinfo.st_mtime))

index = 0
cout = 0
while True:
	tmp_list = os.popen(CMD).read().split('\n')
	# drop the last char, because that's is a space
	tmp_list.pop()
	tmp_list_fileinfo = []
	for tmp_name in tmp_list:
		tmp_file = File()
		tmp_file.filename = tmp_name
		tmp_file.filesize = os.stat(tmp_name).st_size
		tmp_list_fileinfo.append(tmp_file)

	list_files[index] = tmp_list_fileinfo

	
	for old_file in	list_files[0]:
		for new_file in list_files[1]:
			if new_file.filename == old_file.filename:
				if new_file.filesize == old_file.filesize:
					print "file_name:" + new_file.filename

	time.sleep(SLEEP_TIME)
	print "============================="
	if index == 0:
		index = 1
	else:
		index = 0
	cout += 1
