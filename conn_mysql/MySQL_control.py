#!/usr/bin/env python
import progressbar
import os 
import splite_query_sql

START_INDEX = 0
ONCE_HANDLE = 1000

lAll_ID = []


while True:
	result,flag = splite_query_sql.GetProductID(START_INDEX, ONCE_HANDLE)
	
	

	if flag == 1:
		break

	START_INDEX += ONCE_HANDLE

#	result = []
#	for each_id in lAll_ID[:ONCE_HANDLE]:
#		result.append(each_id)
#	input_tmpid_file = open('tmp_product_id', 'w')
#	for each_line in result:
#		input_tmpid_file.write(each_line)
#	input_tmpid_file.close()
#
#	del lAll_ID[0:ONCE_HANDLE]
#
#	if not lAll_ID:
#		break
