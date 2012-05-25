#! /usr/bin/python
import os,time

time2sleep = 2.5
ISOTIMEFORMAT="%Y-%m-%d %X"

while True:
	print time.strftime( ISOTIMEFORMAT, time.localtime())
	print os.popen('top -bi -n 2 -d 0.02').read().split('\n\n\n')[1].split('\n')[2]
	time.sleep(time2sleep)
