# -*- coding: UTF-8 -*-
import os
try:
    #抛出异常
    raise IOError
    # 打开一个文件
    fo = open("E://aa.txt", "r+")
    print "Closed or not : ", fo.closed
    str = fo.read(10);
    print "Read String is : ", str
    fo.seek(0)
    print "Again Read String is : ", fo.read(10);
    # 查找当前位置
    position = fo.tell();
    print "Current file position : ", position
    print "Name of the file: ", fo.name
    print "Opening mode : ", fo.mode
    print "Softspace flag : ", fo.softspace
    fo.close()
    print "Closed or not : ", fo.closed
except IOError:
    print "Error: can\'t find file or read data"
# else:
#     print "Nice"

# 给出当前的目录
print os.getcwd()
#修改名称
# os.rename("E://a.txt", "E://aa.txt")
# 删除一个已经存在的文件test2.txt
# os.remove("E:/a.txt")
# 将当前目录改为"/home/newdir"
# os.chdir("/home/newdir")
# 创建目录test
os.mkdir("E:/test")
#删除目录test
os.rmdir("E:/test")
