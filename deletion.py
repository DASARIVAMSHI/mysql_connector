import mysql.connector as m
mydb = m.connect(host = "localhost",user = "root", password = "root",database = "studentdb")
mycursor=mydb.cursor()
sql1 ="DELETE FROM studentdb WHERE name='vamshi'"
sql2 ="DELETE FROM studentdb WHERE rollno=123"
mycursor.execute(sql1)
mycursor.execute(sql2)
mydb.commit()
"""
# deletion operation
#when ever if you want to delete any type of information which you have created already you can use above command
#Note:you need to select database and you need to select which attribute you are going to delete the data
"""