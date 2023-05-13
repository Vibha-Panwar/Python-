"""
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)
mycursor = mydb.cursor()
mycursor.execute("Create Table Customers2 (name VARCHAR(255), address VARCHAR(255))")
"""

import mysql.connector
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "1q2w!Q@WVibha",
  database = "vibha"  
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)