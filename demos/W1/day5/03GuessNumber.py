'''
·由系统生成一个1000以内的随机三位数
·每次输入一个数来猜取答案
·输出反馈猜大了还是猜小了
·猜到正确的数即结束游戏
'''
import random

answer = random.randint(100, 999)
print(answer)
guess = None

# 只要尚未猜对，就一直循环
while guess != answer:

    # 循环体：猜数字并反馈结果
    guess = eval(input("请输入你的猜想："))
    if guess > answer:
        print("猜大了")
    elif guess < answer:
        print("猜小了")
    else:
        print("猜对了")

print("bye!")
