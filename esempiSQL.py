import mysql.connector

"""
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ll280693!",
    database="",
)

# print(mydb)

myCursor = mydb.cursor()

# sql = "CREATE DATABASE IF NOT EXISTS testdb"

sql = "show databases"

myCursor.execute(sql)

for db in myCursor:
    print(db)
"""
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ll280693!",
    database="testdb",
)

myCursor = mydb.cursor()

#sql = "create table utenti(id int primary key auto_increment, nome varchar(255), cognome varchar(255))"

# myCursor.execute(sql)
# for db in myCursor:
#     print(db)
#  #print("Tabella creata con successo")

"""def insertDB():
    sql = "insert into utenti(nome, cognome) values(%s, %s)"
    val = ("Mario", "Rossi")
    myCursor.execute(sql, val)
    mydb.commit()
    print(myCursor.rowcount, "record inserted.")

insertDB()"""

# FUnzione per inserire più valori in una tabella

def insertValuesDB():
    sql = "insert into utenti(nome, cognome) values(%s, %s)"
    val = [("Mario", "Rossi"), ("Luigi", "Verdi"), ("Anna", "Bianchi")]
    myCursor.executemany(sql, val)
    mydb.commit()
    print(myCursor.rowcount, "record inserted.")

#insertValuesDB()

def selectValue():
    sql = "select * from utenti"
    myCursor.execute(sql)
    myResult = myCursor.fetchone()
    print(myResult)

def selectValues():
    sql = "select * from utenti"
    myCursor.execute(sql)
    myResult = myCursor.fetchall()
    for risultato in myResult:
        print(risultato)
    print(myResult)

#selectValues()
#selectValue()


def deleteValuesDB():
    sql = "delete from utenti where nome = %s and cognome = %s"
    val = ("Mario", "Rossi",)
    myCursor.execute(sql, val)
    mydb.commit()
    print(myCursor.rowcount, "record deleted.")

#deleteValuesDB()