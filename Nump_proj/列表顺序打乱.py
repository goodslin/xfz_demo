import random
import pymysql
import time


def random_list():
    val = [i for i in range(1, 11)]

    random.shuffle(val)

    return val


def timestamp():
    t = time.time()
    return int(t)


def shell_sql():
    db = pymysql.connect("localhost", "root", "Jacklin012", "hongniuhelper")

    cursor = db.cursor()

    ls = random_list()

    t = timestamp()

    sql = "insert into randinfo(win91killNo,win92killNo,win93killNo,win94killNo,win95killNo,win96killNo,win97killNo,win98killNo,win99killNo,win910killNo,win81killNo,win82killNo,win83killNo,win84killNo,win85killNo,win86killNo,win87killNo,win88killNo,win89killNo,win810killNo,kill9,kill8,bettingstatus,usecount,wincount,losecount,nowwincount,nowlosecount,status,bettingcount,createtime,modifytime) \
          values (%s, %s, %s,%s, %s,%s, %s,%s, %s,%s,%s,%s,%s, %s, %s,%s, %s,%s, %s,%s, %s,%s,%s, %s, %s,%s, %s,%s, %s,%s, %s,%s);" \
          % (ls[0], ls[1], ls[2], ls[3], ls[4], ls[5], ls[6], ls[7], ls[8], ls[9], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, t, t)

    # try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    # except:
    #     # 如果发生错误则回滚
    #     db.rollback()
    #     # 关闭数据库连接
    db.close()


# i = 1
# while i < 30:
#     shell_sql()
#     i += 1
shell_sql()