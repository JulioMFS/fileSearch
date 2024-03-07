
import pymysql

#database connection
connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="j301052", database="test")
cursor = connection.cursor()

# queries for inserting values
insert1 = "INSERT INTO Artists(NAME, TRACK) VALUES('Towang', 'Jazz' );"
insert2 = "INSERT INTO Artists(NAME, TRACK) VALUES('Sadduz', 'Rock' );"

#executing the quires
cursor.execute(insert1)
cursor.execute(insert2)


#commiting the connection then closing it.
connection.commit()
connection.close()
