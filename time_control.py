#!/usr/bin/env python

import time, os

MINUTE = 60
HOUR = 3600
SLEEP_TIME = 30

CMD = 'python py_client.py'

while True:
	current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	if os.popen(CMD).read() == "ok\n":
		print "success:" + current_time
	else:
		print "fails:" + current_time

	time.sleep(SLEEP_TIME)
