import mysql.connector
connection = mysql.connector.connect(user="root", password="", host="localhost")
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Adharcard")
connection = mysql.connector.connect(user="root", password="", host="localhost", database = "Adharcard")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Information (name VARCHAR(15), age VARCHAR(15), gender VARCHAR(7), d_o_b VARCHAR(20), Father_name VARCHAR(40))")
bb="INSERT INTO Information (name,age,gender,d_o_b,Father_name) VALUES (%s,%s,%s,%s,%s)"
cc= [
    ('sowmiya','15','female','29/04/2001','ravi'),
('abhinaya','16','female','08/05/2001','sundar'),
('yeshwanth','25','male','02/09/1998','vetri'),
('yogesh','45','male','11/12/1985','suresh'),
('shakti','30','female','22/03/2001','elumazhai')
]
cursor.executemany(bb,cc)
connection.commit