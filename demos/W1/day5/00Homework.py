'''
# 4.08 输入三个任意数，升序排序输出
# 4.11 输入任意六位数月份（201711），输出这个月有多少天
# 4.12 判断输入的数是否被5整除，是否被6整除，是否同时被5和6同时整除
# 4.16 输出一个随机大写字母
# 4.19 随意输入三个数，判断能否形成三角形
'''
import os
import random

import sys


def answer408():
    a, b, c = eval(input("输入三个数"))
    theMin = min(a, b, c)
    theMax = max(a, b, c)
    theMiddle = None

    if a > theMin and a < theMax:
        theMiddle = a
    elif b > theMin and b < theMax:
        theMiddle = b
    else:
        theMiddle = c

    print(theMin, theMiddle, theMax)

def answer411():
    uInput = int(input("输入六位数月份"))
    year = uInput // 100
    month = uInput % 100
    if not (month > 0 and month < 13):
        print("输入不合法，您的智力水平还不能使用本软件，祝您生活愉快，再见！")
        sys.exit()#退出程序

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        ret = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        ret = 30
    elif month == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        ret = 29
    else:
        ret = 28

    print("该约有%d天"%(ret))

def answer412():
    uInput = int(input("请输入一个数"))
    if uInput % 5 == 0 and uInput % 6 == 0:
        print("被5、6同时整除")
    elif uInput % 5 == 0:
        print("能被5整除")
    elif uInput % 6 == 0:
        print("能被6整除")
    else:
        print("不能整除")

def answer416():
    start = ord("A")
    end = ord("Z")
    letterOrder = random.randint(start,end)
    letter = chr(letterOrder)
    print(letter)

def answer419():
    a,b,c = eval(input("输入三条边的长度"))
    if ((a+b>c)and(a+c>b)and(b+c>a)) \
            and ((abs(a-b)<c)and(abs(a-c)<b)and(abs(b-c)<a)):
        print("可以构成三角形")
    else:
        print("不能构成三角形")

# answer408()
# answer411()
# answer412()
# answer416()
# answer419()
