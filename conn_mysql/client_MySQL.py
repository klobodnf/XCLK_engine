#!/usr/bin/env python
import MySQLdb

HOST_NAME = "10.188.53.246"
USERNAME = "dev"
PASSWORD = "dev@mysql5.5"
DATABASE = "recommender"

def GetProductID():
	conn = MySQLdb.connect(host=HOST_NAME, user=USERNAME, passwd=PASSWORD, db=DATABASE)

	cursor = conn.cursor()

	cursor.execute("""select ID from  product;""")
	product_table_tuple =  cursor.fetchall()
	#for msg in cursor.fetchall():
		## because type of msg is tuple
	#	print msg[0]
	cursor.close()
	return product_table_tuple
print GetProductID()
