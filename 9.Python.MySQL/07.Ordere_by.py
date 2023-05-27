## Order by statement used to sort the result in Ascending or Descending order.
## By Default, Order by function sort the value in ascending order. 
## If you want the result in the descending order then use the DESC keyword.

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)

mycursor = mydb.cursor()
sql = "select * FROM customers ORDER BY name"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


## Order by Descending order:-->

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
