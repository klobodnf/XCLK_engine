#!/usr/bin/env python
import MySQLdb
import progressbar

HOST_NAME = "10.188.53.246"
USERNAME = "dev"
PASSWORD = "dev@mysql5.5"
DATABASE = "recommender"

def GetProductID():
	conn = MySQLdb.connect(host=HOST_NAME, user=USERNAME, passwd=PASSWORD, db=DATABASE)

	cursor = conn.cursor()
	ALL_RESULT = []

	cursor.execute("""SELECT DISTINCT ID FROM product WHERE sale_flag = 1;""")
	product_table_tuple =  cursor.fetchall()
	progress = progressbar.ProgressBar()
	for msg in progress(product_table_tuple):
		print msg[0]
	cursor.close()
	return ALL_RESULT
GetProductID()
