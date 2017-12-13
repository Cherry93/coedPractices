'''
·生成随机两位数作为中奖密码
·用户输入一个两位数
·如果全等于中奖密码，特等奖
·如果数字和中奖密码相同，大奖
·有一个数字相同，安慰奖
·否则没奖
'''
import random

luckyCode = random.randint(10, 99)
print("本期双色球中奖号码为：%d"%(luckyCode))
myCode = int(input("骚年请输入你猜想："))
# 23
# 32

# 提取出中奖码的十位、个位
lucky1 = luckyCode // 10  # 提取十位
lucky2 = luckyCode % 10  # 提取个位
m1 = myCode // 10
m2 = myCode % 10

if myCode == luckyCode:
    print("一等奖")

elif m1 == lucky2 and m2 == lucky1:
    print("二等奖")

elif m1 == lucky1 or m1 == lucky2 or m2 == lucky1 or m2 == lucky2:
    print("安慰奖")

else:
    print("没奖")
