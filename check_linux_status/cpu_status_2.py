#! /usr/bin/python
import os

def cpu_status():
	cpu_status = []

	for percent in  os.popen('top -bi -n 2 -d 0.02').read().split('\n\n\n')[1].split('\n')[2].split('%'):
		if percent != "st":
			if percent.find(':') != -1:
				cpu_status.append(percent.split(':')[1].strip())
			else:
				cpu_status.append(percent.split(',')[1].strip())


	return float(cpu_status[3])

#print cpu_status()
