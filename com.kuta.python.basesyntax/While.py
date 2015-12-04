# -*- coding: UTF-8 -*-
#while循环
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"

# continue 和 break 用法
i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print i         # 输出双数2、4、6、8、10
i = 1
while 1:            # 循环条件为1必定成立
    while (1):
        if i > 2:
            break
        print("xxx")
        break
    print i         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break