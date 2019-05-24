import pymysql

conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="jacklin012",db="water",charset="utf8")

cur = conn.cursor()

sql = "select * from w_test1;"

cur.execute(sql)

rows = cur.fetchall()

for dr in rows:
    print(dr)
 