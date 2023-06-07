## Drop Table :--> means delete complete tables in one go.
"""
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)

mycursor = mydb.cursor()
sql = "Drop Table customers"
mycursor.execute(sql)

"""
### Drop Table Only If Exits :-->
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)

mycursor = mydb.cursor()
sql ="DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
