## we can control the output in quantity like how many records we want in the output.
## For this we will use 'limit'statement.

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)
mycursor = mydb.cursor()
mycursor.execute("select * from customers2 limit 5")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


## Start from another position :-->

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)
mycursor = mydb.cursor()
mycursor.execute("select * from customers2 limit 5 offset 3")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)