import pymysql

db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    charset = "utf8")

cursor = db.cursor(pymysql.cursors.DictCursor)

cursor.execute('USE blog;')
# cursor.execute('INSERT INTO test (Color, Count) VALUES("yellow", 2)')
cursor.execute('SELECT * FROM test;')
value = cursor.fetchall()

print(value[0])

db.commit()
db.close()