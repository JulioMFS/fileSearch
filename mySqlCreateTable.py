
import pymysql

#database connection
connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="j301052", database="ponte")
cursor = connection.cursor()
# Query for creating table
ArtistTableSql = """CREATE TABLE Artists(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME  CHAR(20) NOT NULL,
TRACK CHAR(10))"""

cursor.execute(ArtistTableSql)
connection.close()
