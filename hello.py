# -*- coding: UTF-8 -*-
import A
# str =raw_input("Enter you input:")
# 字符串类型
str = """你好
asadd"""
# del str
print str.decode('utf8')[0:3].encode('utf8')
print(str); 

# 列表类型
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print list # 输出完整列表
print list[0] # 输出列表的第一个元素
print list[1:3] # 输出第二个至第三个的元素
print list[2:] # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2 # 输出列表两次
print list + tinylist # 打印组合的列表

print A.a
print dir(A)