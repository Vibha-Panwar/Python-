## Select all the record from the database and display it.
## Fetchall() 
"""
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers") # [give * for selecting all the data]
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT name, address FROM customers") # [Or we can simply say the exect column which we wanna fetch]
myresult = mycursor.fetchall()  #[this condition can happen only if we know what are column present in the database.]
for x in myresult:
    print(x)
"""

## Fetchone() method:-->

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)