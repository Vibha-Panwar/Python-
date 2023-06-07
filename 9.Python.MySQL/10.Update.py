
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




import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1q2w!Q@WVibha",
    database = "vibha"
)
mycursor = mydb.cursor()
mycursor.execute("show tables")

for x in mycursor:
    print(x)






import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1q2w!Q@WVibha",
  database="vibha"
)
mycursor = mydb.cursor()
sql = "insert into customers2 (name,address) values (%s,%s)"
val = [
    ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")


### Updating the table:-->

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="1q2w!Q@WVibha",
    database = "vibha"
)
mycursor = mydb.cursor()
sql = "update customers2 set address = 'canyon 123' where address = 'valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")