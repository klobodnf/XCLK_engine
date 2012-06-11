#!/usr/bin/env python

import os
import time
CMD = 'echo "jjdsfs" >> README.md'

H = 3600
M = 60

SLEEP_TIME = 5

while True:
	os.popen(CMD)
	time.sleep(SLEEP_TIME)
