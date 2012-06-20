#!/usr/bin/env python
import MySQLdb

HOST_NAME = "10.188.53.246"
USERNAME = "dev"
PASSWORD = "dev@mysql5.5"
DATABASE = "recommender"

def GetProductID():
	conn = MySQLdb.connect(host=HOST_NAME, user=USERNAME, passwd=PASSWORD, db=DATABASE)

	cursor = conn.cursor()

	#cursor.execute("""select THIRD_ASSORT_CODE from dw_merchandise_base_assort;""")
	#cursor.execute("""select * from product WHERE ID = 1000000;""")
	#cursor.execute("""desc dw_merchandise_base_assort;""")
	#cursor.execute("""SELECT THIRD_ASSORT_CODE FROM dw_merchandise_base_assort WHERE MERCHANDISE_ID = 1000170;""")
	cursor.execute("""SELECT product.ID, dw_merchandise_base_assort.FIRST_ASSORT_CODE, dw_merchandise_base_assort.SECOND_ASSORT_CODE, dw_merchandise_base_assort.THIRD_ASSORT_CODE FROM product, dw_merchandise_base_assort WHERE dw_merchandise_base_assort.MERCHANDISE_ID = product.ID and product.ID=1000000;""")
	product_table_tuple =  cursor.fetchall()
	for msg in product_table_tuple:
		## because type of msg is tuple
		print msg
	cursor.close()
GetProductID()
