## We can delete record from the database by using the "DELETE" from statement.
"""
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)
mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address ='Highway 11'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) deleted")
"""

## Prevent SQL Injection:-->
