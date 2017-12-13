'''
·能被4整除但不能被100整除的年是闰年
·400的整数倍年是闰年
'''

year = int(input("请输入年份"))

# isLeapYear,布尔类型初值，默认假
isLeapYear = False

# 如果是闰年，isLeapYear赋值为真，否则为假
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    isLeapYear = True
else:
    isLeapYear = False

# 根据isLeapYear的真假做具体打印
if isLeapYear == True:
    print("是闰年")
else:
    print("不是闰年")
