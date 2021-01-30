import mysql.connector as m
mydb = m.connect(host = "localhost",user = "root", password = "root",database = "studentdb")
mycursor=mydb.cursor()
mycursor.execute("select * from studentdb")
print(mydb)
"""
#read command 
#when you have inserted the values and you need to check whether the values are inserted or not we use read command
#select *from database
"""