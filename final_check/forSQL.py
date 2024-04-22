import pymysql

con = pymysql.connect(host="localhost",user= "root",password="omdevansh24", db="studentmanagementsystem1")
cursor = con.cursor()
cursor.execute("select * from studentattendance1")
output = cursor.fetchall()

print(output)