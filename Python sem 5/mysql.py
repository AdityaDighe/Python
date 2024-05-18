import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass@123",
)

mycursor= mydb.cursor()
mycursor.execute("show databases")
for x in mycursor:
    print(x)