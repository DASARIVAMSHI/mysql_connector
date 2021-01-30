import mysql.connector as m
mydb = m.connect(host = "localhost",user = "root", password = "root",database = "studentdb")
mycursor=mydb.cursor()
mycursor.execute("insert into studentdb(name,rollno) values('vamshi',190330272)")
mydb.commit()
print(mydb)
"""
# insertion #
# after the creation of table you need to insert the values to the particualr database
# note:with out creating table you cannot insert values into a database
#It will dispaly the values which you have inserted!!
"""