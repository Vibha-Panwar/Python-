## Where function is used when we select something perticular 
## from a database and for this we need to filter the data.
"""
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address = 'highway'"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)



## Wildcard Character:

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address LIKE '%village%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
"""
