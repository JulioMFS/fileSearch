import pymysql

#database connection
connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="j301052", database="agro")
cursor = connection.cursor()

# queries for retrievint all rows
retrive = "Select * from parcela;"

#executing the quires
cursor.execute(retrive)
rows = cursor.fetchall()
for row in rows:
   print(row)


#commiting the connection then closing it.
connection.commit()
connection.close()

