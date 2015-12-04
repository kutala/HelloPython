# -*- coding: UTF-8 -*-
 
#可写函数说明
def printinfo( name, sex , age = 35):
   "打印任何传入的字符串"
   print "Name: ", name;
   print "Age ", age;
   print "Sex", sex;
   return;
 
#调用printinfo函数
printinfo( age=50, name="miki", sex = 1 );
# printinfo( 1, name="miki" );


# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      print "*", var
   return;
 
# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50 );

# 匿名函数
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;
 
# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )
print "相加后的值为 : ", sum( 20, 20 )

#函数作用域
total = 0; # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2; # total在这里是局部变量.
   print "函数内是局部变量 : ", total
   return total;
 
#调用sum函数
sum( 10, 20 );
print "函数外是全局变量 : ", total 
