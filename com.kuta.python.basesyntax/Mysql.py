# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("192.168.37.11","testUser","test1234","mall_apartment" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()

print "Database version : %s " % data

# 创建数据表SQL语句
cursor.execute("""SELECT * FROM ap_apartment limit 0, 10""")
data = cursor.fetchall();
rowcount = cursor.rowcount
print "共有%d行数据" % rowcount
for row in data:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # 打印结果
      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )

# 关闭数据库连接
db.close()