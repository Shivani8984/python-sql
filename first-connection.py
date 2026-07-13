# import mysql.connector as dbconnect

# myconnection = dbconnect.connect(host='localhost', database='classicmodels', user='root', password='password')

# if myconnection.is_connected():
#     print('Successfully Connected to MySQL database')

# # Get a cursor
# cursor = myconnection.cursor()
# SQLQuery ="SELECT ordernumber, SUM(quantityOrdered) AS itemsCount, SUM(priceeach*quantityOrdered) AS total FROM orderdetails GROUP BY ordernumber HAVING    total > 1000    AND    itemsCount > 600";
# # Execute a query
# cursor.execute(SQLQuery)            
# # get all records
# records = cursor.fetchall()   
# print("Total number of rows in table: ", cursor.rowcount)    
# print("\nPrinting each row")
# for row in records:
#     print("order number = ", row[0],  )
#     print("item counts = ", row[1])
#     print("total  = ", row[2], "\n" )
# # Close connection
# cursor.close()
# myconnection.close()


import mysql.connector as mydbconnection
from mysql.connector import Error
conn = mydbconnection.connect(database='usersdb', user='root',password='password', port ='3306')
cursor=conn.cursor()
myquery = "CREATE TABLE tasks (task_id INT AUTO_INCREMENT,title VARCHAR(255) NOT NULL,\
start_date DATE,\
due_date DATE,\
priority TINYINT NOT NULL DEFAULT 3,\
description TEXT,\
PRIMARY KEY (task_id))"
cursor.execute(myquery)
