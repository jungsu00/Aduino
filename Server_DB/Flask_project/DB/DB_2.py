import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    passwd="1234",
    db="blog",
    charset="utf8")
    
cursor = db.cursor()

sql = "SELECT * from test"
cursor.execute(sql)
value = cursor.fetchall()

print(value[0])
print(value[1])
print(value[2])