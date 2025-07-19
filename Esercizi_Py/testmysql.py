import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ll280693!",
    database="",
)

#print(mydb) 

myCursor = mydb.cursor()

#sql = "CREATE DATABASE IF """NOT EXISTS""" testdb"

sql = "show databases"

myCursor.execute(sql)

for db in myCursor:
    print(db)