"""
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers(name, address) VALUES(%s, %s)"
val = ("JOHN", "Highway 11")
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount,"record inserted.")

## Insert many rows in one go.
## executemany() - list of many tuples

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers(name, address) VALUES(%s, %s)"
val = [
    ('Peter', 'street 21'),
    ('Amy', 'street 22' ),
    ('Jonny', 'street 34'),
    ('Vickey', 'Yellow Garden 2')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount,"was inserted.")
"""
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers(name, address) value(%s, %s)"
val = ("Micelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)