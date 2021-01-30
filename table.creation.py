import mysql.connector as m

mydb = m.connect(host = "localhost",user = "root",password = "root",database="studentdb")
mycursor=mydb.cursor()
mycursor.execute("create table studentdb (name varchar(20),rollno int)")
"""
# now table creation 
# when ever if you want to create any table or to perform any specific task you need you select database First
# ex:show databases;(command) It will dispaly the databases which are available in your mysql
# use databases; (command) you will select a patricular database which you want to create any table or to perform 
# any specific tasks
#syntax:create table name of the table(required attributes and we must specify the data type..
#as we know for string we declare varchar(20) for intergers we declare int..
#ex:("create table circle(area varchar(20),radius int)")
#after creation of the table it will be displayed as table created
"""