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
		## because type of msg is tuple
		SQL = """SELECT product_id,cat_id FROM site_cat_prd_relation_1001 WHERE product_id=""" + str(msg[0])  + """;"""
	#	print SQL
		cursor.execute(SQL)
		tmp_result = cursor.fetchall()
		if tmp_result:
			ALL_RESULT.append(tmp_result)

	cursor.close()
	return ALL_RESULT
#print GetProductID()
