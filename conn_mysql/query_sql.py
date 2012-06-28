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

	#cursor.execute("""select THIRD_ASSORT_CODE from dw_merchandise_base_assort;""")
	#cursor.execute("""select * from product WHERE ID = 1000000;""")
	# ('product_id', 'varchar(255)', 'NO', 'MUL', None, '')
	#('cat_id', 'char(255)', 'NO', '', None, '')
	
	#cursor.execute("""desc product;""")
	#cursor.execute("""SELECT product_id, cat_id FROM site_cat_prd_relation_1001;""")
 	cursor.execute("""SELECT DISTINCT ID FROM product WHERE sale_flag = 1 LIMIT 1000""")
	#cursor.execute("""show tables;""")
	#cursor.execute("""SELECT THIRD_ASSORT_CODE FROM dw_merchandise_base_assort WHERE MERCHANDISE_ID = 1000170;""")
	#cursor.execute("""SELECT product.ID, dw_merchandise_base_assort.FIRST_ASSORT_CODE, dw_merchandise_base_assort.SECOND_ASSORT_CODE, dw_merchandise_base_assort.THIRD_ASSORT_CODE FROM product, dw_merchandise_base_assort WHERE dw_merchandise_base_assort.MERCHANDISE_ID = product.ID and product.ID=1000000;""")
	product_table_tuple =  cursor.fetchall()
	progress = progressbar.ProgressBar()
	for msg in progress(product_table_tuple):
		## because type of msg is tuple
		SQL = """SELECT product_id,cat_id FROM site_cat_prd_relation_1001 WHERE product_id=""" + str(msg[0])  + """;"""
#		#print SQL
		cursor.execute(SQL)
#		ALL_RESULT.append(cursor.fetchall())
#
	cursor.close()
#	return ALL_RESULT
GetProductID()
