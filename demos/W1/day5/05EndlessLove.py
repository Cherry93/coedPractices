'''
·输入一个人的名字，将“我爱XX”输出100遍
·使用for循环做
-----
·输入两个名字AA、BB
·逢五输出“我爱BB”，否则输出“我爱AA”
·总输出为100遍
'''
import time

count  = 0
# while count < 100:
#     print("我爱拉芳")
#     time.sleep(1)
#     count += 1

# 1.0,start=0,end=10,下标范围0-9（含头不含尾）
# for i in range(10):
#     print("我爱拉芳",i)
#     time.sleep(1)

# for i in range(100):
#     if i % 10 == 0:
#         print("拉芳",i)
#     else:
#         print("潘婷",i)

# 2.0,start=1,end=101,下标范围1-100（含头不含尾）
# for i in range(1,101):
#     if i % 10 == 0:
#         print("拉芳",i)
#     else:
#         print("潘婷",i)

#3.0 start = 1,end=101,步长step=5,下标范围（1,6,11...96）
for i in range(1,101,5):
    if i % 10 == 0:
        print("拉芳",i)
    else:
        print("潘婷",i)
