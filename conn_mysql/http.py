#!/usr/bin/env python

import urllib2
import httplib
import socket
import re
import client_MySQL


FLAG_TIMEOUT		= 0x0001
FLAG_NOTFOUND 		= 0x0002
FLAG_BROKEN			= 0x0010
FLAG_NOT_ENOUGH 	= 0x0020
FLAG_NOT_MATCH 		= 0x0100
FLAG_OK 			= 0x0200

FLAG_STATUS		= 0x0000

BOOL_PRODUCT_A = 0x0001
BOOL_PRODUCT_B = 0x0010
BOOL_PRODUCT_C = 0x0100

PRODUCT_STATUS = 0x0000

print "now get the product id... please wait!"
ALL_PRODUCT_ID = client_MySQL.GetProductID()
print "now check the all link.."
ALL_PRODUCT_POOL = []

## this just for test mode
# test start######
TEST_CHECK_NUM = 1000
ALL_PRODUCT_ID = ALL_PRODUCT_ID[:TEST_CHECK_NUM]
# test end ######

COUNT = 0
DISPLAY_NUM = 10
USER_ID = "Ls8Y2Pe7k32w8R8lcSkR"

def CheckProductIsRight(URL):
	global FLAG_TIMEOUT		
	global FLAG_NOTFOUND 	
	global FLAG_BROKEN		
	global FLAG_NOT_ENOUGH 	
	global FLAG_NOT_MATCH 	
	global FLAG_OK 			
	
	## reset this flag every time.
	FLAG_STATUS     = 0x0000

	print URL
	
	## check the URL is OK?
	try:
		#~ print URL.split('/')[2]
		#~ conn = httplib.HTTPConnection("weibo.com", timeout=2)
		conn = httplib.HTTPConnection(URL.split('/')[2], timeout=2)
		conn.request("GET", "/")
		r1 = conn.getresponse()
		#~ print r1.status, r1.reason
		if r1.status == 404:
			FLAG_STATUS = FLAG_STATUS | FLAG_NOTFOUND
			return FLAG_STATUS
			print "this link has been not found!"
	except socket.timeout:
		print "this link has been time out!"
		FLAG_STATUS = FLAG_STATUS | FLAG_TIMEOUT
		return FLAG_STATUS
	except socket.error:
		print "this link has been broken!"
		FLAG_STATUS = FLAG_STATUS | FLAG_BROKEN
		return FLAG_STATUS

	try:
		opener = urllib2.build_opener()
		f = opener.open(URL)
		HTML_SOURCE_CODE = f.read()

		pattern = re.compile(r'"id":"\d+"')
		match = pattern.findall(HTML_SOURCE_CODE)

		if match:
			#print len(match)
			if len(match) == DISPLAY_NUM:
				FLAG_STATUS = FLAG_STATUS | FLAG_OK
				return FLAG_STATUS
			else:
				FLAG_STATUS = FLAG_STATUS | FLAG_NOT_ENOUGH
				return FLAG_STATUS
			#~ for msg in match:
				#~ ID_CODES.append(msg.split('"')[3])
		else:
			FLAG_STATUS = FLAG_STATUS | FLAG_NOT_MATCH
			return FLAG_STATUS
	except urllib2.HTTPError:
		print "this link has been not found!"
		FLAG_STATUS = FLAG_STATUS | FLAG_NOTFOUND
		return FLAG_STATUS


##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################

		
for product in ALL_PRODUCT_ID:
	
	#111 equal three,two,one is normal
	product_item = [product[0], PRODUCT_STATUS]
	
	URL_one = "http://10.188.53.247:8080/recommend/vav?userId=" + USER_ID + "&productId=" + str(product[0]) + "&num=" + str(DISPLAY_NUM) + "&callback=callback&catId=" + str(product[1])
	URL_two = "http://10.188.53.247:8080/recommend/vav?userId=" + USER_ID + "&productId=" + str(product[0]) + "&num=" + str(DISPLAY_NUM) + "&callback=callback&catId=" + str(product[2])
	URL_three = "http://10.188.53.247:8080/recommend/vav?userId=" + USER_ID + "&productId=" + str(product[0]) + "&num=" + str(DISPLAY_NUM) + "&callback=callback&catId=" + str(product[3])
	
	print "product id:" + str(product[0])
	

	tmp_result = CheckProductIsRight(URL_one)
	#~ print "%x" %tmp_result
	if  tmp_result & FLAG_OK:
		product_item[1] = product_item[1] | BOOL_PRODUCT_A
		print "A is OK."
	else:
		print "A is ERROR."
	print "========================"
	
		
	
	tmp_result = CheckProductIsRight(URL_two)
	#~ print "%x" %tmp_result
	if  tmp_result & FLAG_OK:
		product_item[1] = product_item[1] | BOOL_PRODUCT_B
		print "B is OK."
	else:
		print "B is ERROR."

	print "========================"
	
	
	tmp_result = CheckProductIsRight(URL_three)
	#~ print "%x" %tmp_result
	if  tmp_result & FLAG_OK:
		product_item[1] = product_item[1] | BOOL_PRODUCT_C
		print "C is OK."
	else:
		print "C is ERROR."

		
	ALL_PRODUCT_POOL.append(product_item)
	COUNT += 1
	print COUNT
	print "*** * *** * *** * *** * *** * *** * *** *"
	print "*** * *** * *** * *** * *** * *** * *** *"
	
for result in ALL_PRODUCT_POOL:
	#print "nHex = %x,nDec = %d,nOct = %o" %(nHex,nHex,nHex)
	print "[%d, %x]" %(result[0], result[1])
