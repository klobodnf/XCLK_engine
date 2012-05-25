#! /usr/bin/python
import os,time

time2sleep = 10
ISOTIMEFORMAT="%Y-%m-%d %X"

while True:
	print time.strftime( ISOTIMEFORMAT, time.localtime())
	for percent in  os.popen('top -bi -n 2 -d 0.02').read().split('\n\n\n')[1].split('\n')[2].split('%'):
		if percent != "st":
			if percent.find(':') != -1:
				print percent.split(':')[1].strip()
			else:
				print percent.split(',')[1].strip()
	time.sleep(time2sleep)

