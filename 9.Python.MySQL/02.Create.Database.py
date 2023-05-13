'''
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

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
'''

## Try connecting to the Database:--

import mysql.connector

mydb= mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE vibha")

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name TEXT(10),address VARCHAR(30))")
mycursor.execute("SHOW TABLES")

for i in mycursor:
    print(i)