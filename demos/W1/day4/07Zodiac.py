'''
·2000年是龙年
·输入任意年份，判断生肖
'''

# 年份对12求余
# 4-子鼠
# 5-丑牛
# 6-寅虎
# 7-卯兔
# 8-辰龙
# 9-巳蛇
# 10-午马
# 11-未羊
# 0-申猴
# 1-酉鸡
# 2-戌狗
# 3-亥猪

year = int(input("请输入任意年份："))
odd = year % 12

if odd == 4:
    print("子鼠")
elif odd == 5:
    print("丑牛")
elif odd == 6:
    print("寅虎")
elif odd == 7:
    print("卯兔")
elif odd == 8:
    print("辰龙")
elif odd == 9:
    print("巳蛇")
elif odd == 10:
    print("午马")
elif odd == 11:
    print("未羊")
elif odd == 0:
    print("申猴")
elif odd == 1:
    print("酉鸡")
elif odd == 2:
    print("戌狗")
else:
    print("亥猪")
