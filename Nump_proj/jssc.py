import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Jacklin012', db='jssc')

cursor = conn.cursor()

data = 1

sql = "select wan from fastlotteryinfo;"

cursor.execute(sql)

li = []
ls = []
for row in cursor.fetchall():
    # print("Num. -%s" %row)
    li.append(list(row))
    # print(type(row))
# print((li[0][0]))
# print(len(li))

# 依次取出列表中的数据
i = 0
a = 0
b = 0

try:
    while i < len(li):

        kaijiang_num = li[i + 1][0]
        zhongjiang_num = li[i][0]

        if kaijiang_num == 0:
            ls = [0, 1, 2, 3, 7, 8, 9]
        elif kaijiang_num == 1:
            ls = [0, 1, 2, 3, 4, 8, 9]
        elif kaijiang_num == 2:
            ls = [0, 1, 2, 3, 4, 5, 9]
        elif kaijiang_num == 3:
            ls = [0, 1, 2, 3, 4, 5, 6]
        elif kaijiang_num == 4:
            ls = [1, 2, 3, 4, 5, 6, 7]
        elif kaijiang_num == 5:
            ls = [2, 3, 4, 5, 6, 7, 8]
        elif kaijiang_num == 6:
            ls = [3, 4, 5, 6, 7, 8, 9]
        elif kaijiang_num == 7:
            ls = [0, 4, 5, 6, 7, 8, 9]
        elif kaijiang_num == 8:
            ls = [0, 1, 5, 6, 7, 8, 9]
        elif kaijiang_num == 9:
            ls = [0, 1, 2, 6, 7, 8, 9]

        """
        if kaijiang_num == 0:
            ls = [0, 1, 2, 3, 7, 8, 9, 4, 6]
        elif kaijiang_num == 1:
            ls = [0, 1, 2, 3, 4, 8, 9, 5, 7]
        elif kaijiang_num == 2:
            ls = [0, 1, 2, 3, 4, 5, 9, 6, 8]
        elif kaijiang_num == 3:
            ls = [0, 1, 2, 3, 4, 5, 6, 7, 9]
        elif kaijiang_num == 4:
            ls = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        elif kaijiang_num == 5:
            ls = [2, 3, 4, 5, 6, 7, 8, 1, 9]
        elif kaijiang_num == 6:
            ls = [3, 4, 5, 6, 7, 8, 9, 2, 0]
        elif kaijiang_num == 7:
            ls = [0, 4, 5, 6, 7, 8, 9, 3, 2]
        elif kaijiang_num == 8:
            ls = [0, 1, 5, 6, 7, 8, 9, 4, 2]
        elif kaijiang_num == 9:
            ls = [0, 1, 2, 6, 7, 8, 9, 5, 3]
        """



        if zhongjiang_num in ls:
            a += 1
            print('赢')
        else:
            b -= 1
            print('////////////')
        i += 1
except Exception as e:
    pass

# print(li[1][0])  # 0
# print(li[0][0])  # 9
print(a)
print(b)