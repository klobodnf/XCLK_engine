#!/usr/bin/env python
import os


CMD = "cat /proc/loadavg | awk '{print $3}'"

def loadavg_stat():
	loadavg =  os.popen(CMD).read().split('\n')[0]
	return loadavg
