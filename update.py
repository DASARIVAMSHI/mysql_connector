import mysql.connector as m
mydb = m.connect(host = "localhost",user = "root", password = "root",database = "studentdb")
mycursor=mydb.cursor()
sql ="Update studentdb SET rollno=123 WHERE name='vamshi'"
mycursor.execute(sql)
mydb.commit()
"""
#update command 
#now if you have already created a database if you forget to insert a value then you can use the above command to update the data
#you need to select update and select database set what you want to insert and select where you want to insert 
"""