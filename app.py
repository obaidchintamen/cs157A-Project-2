# Kevin's using python connect to mysql workbench

import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='aaa123123123')

mycursor = mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)