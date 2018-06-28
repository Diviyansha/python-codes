#!/usr/bin/python
import mysql.connector as mysql
con=mysql.connect(user='root', password='red123', host='localhost', database='adhoc1')
print"1.INSERT"
print"2.DISPLAY"
print"3.UPDATE"
print"4.DELETE"
choice=raw_input("enter choice")
cur=con.cursor()
if choice=='1':
	cur.execute("insert into student(name,email) values ('muskan','muskan@gmail.com')")
	print"inserted"
	
elif choice=='2':
	cur.execute("select name from student")
	output=cur.fetchall()
	print output
elif choice=='3':
	cur.execute("update student set name='anvita' where name='monika'")
	print"updated"
	
elif choice=='4':
	cur.excute("delete from student where name='anvita'")
	print"deleted"
con.commit()
