import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Jacklin012', db='hongniuhelper')

# 游标
cursor = conn.cursor()

# sql = "CREATE TABLE TEST(id INT,name VARCHAR(20))"
# cursor.execute(sql)

# ret = cursor.execute("INSERT INTO TEST VALUES (1,'alex'),(2,'egon')")

# RET = cursor.execute("SELECT * FROM TEST;")
#
# print(RET)
# cursor.scroll(-1, mode="relative")
#
# print(cursor.fetchmany(3))
#
# conn.commit()
# cursor.close()
# conn.close()


# try:
#     insertSQL0 = "INSERT INTO ACCOUNT2 (name,balance) VALUES ('oldboy',4000)"
#     insertSQL1 = "UPDATE account2 set balance=balance-30 WHERE name='yuan'"
#     insertSQL3 = "UPDATE account2 set balance=balance+30 WHERE name='xialv'"
#
#     cursor = conn.cursor()
#     cursor.execute(insertSQL0)
#     conn.commit()
#
#     cursor.execute(insertSQL2)
#     cursor.close()
#     conn.commit()
#
# except Exception as e:
#     conn.rollbcak()
#     conn.commit()
#
# cursor.close()
# conn.close()

from hashlib import md5

# s = 'How to use md5 in python hashlib'
# e = md5(s.encode('utf-8'))
# print(e.hexdigest())

