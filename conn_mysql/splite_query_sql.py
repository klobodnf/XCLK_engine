#!/usr/bin/env python
import MySQLdb
import progressbar

HOST_NAME = "10.188.53.246"
USERNAME = "dev"
PASSWORD = "dev@mysql5.5"
DATABASE = "recommender"


#START_INDEX = 0
#ONCE_HANDLE = 1000

def GetProductID(START_INDEX, ONCE_HANDLE):
	FLAG = 0
	conn = MySQLdb.connect(host=HOST_NAME, user=USERNAME, passwd=PASSWORD, db=DATABASE)
	cursor = conn.cursor()

	cursor.execute("""SELECT DISTINCT ID FROM product WHERE sale_flag = 1 LIMIT """ + str(START_INDEX) + """,""" +  str(ONCE_HANDLE))
	product_table_tuple =  cursor.fetchall()

	if(len(product_table_tuple) < ONCE_HANDLE):
		FLAG = 1
	
	progress = progressbar.ProgressBar()


	tmp_str = ""
	for msg in progress(product_table_tuple):
		tmp_str += str(msg[0]) + ','
	
	SQL = """SELECT product_id,cat_id FROM site_cat_prd_relation_1001 WHERE product_id in (""" + tmp_str[:-1]  + """);"""

#	print SQL
	cursor.execute(SQL)
	ALL_RESULT =  cursor.fetchall()
	cursor.close()
	return ALL_RESULT, FLAG

#r1, r2 = GetProductID(START_INDEX, ONCE_HANDLE)
#print r1
