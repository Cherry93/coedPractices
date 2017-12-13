'''
·逻辑同1.0
·将-1设置为管理员终止密码，一旦如输入-1则提前终止游戏
-----
·如果用户输入不在范围内，提示“傻鸟，必须输入1-1000以内的数”，重新猜
'''
import random
'''
break = 暴力地立即终止循环
continue = 忽略本次循环的未完成部分，进入下一次循环
'''

answer = random.randint(100, 999)
# print(answer)
guess = None

# 只要尚未猜对，就一直循环
while guess != answer:

    guess = eval(input("请输入你的猜想："))

    # 判断用户是否想暴力终止游戏
    if guess == -1:

        # 立即终止循环
        break

    # 如果输入不合法
    if not (guess > 99 and guess < 1000):
        print("傻鸟，必须输入1-1000以内的数")

        # 忽略本次循环的未完成部分，进入下一次循环
        continue

    # 反馈猜想结果
    if guess > answer:
        print("猜大了")
    elif guess < answer:
        print("猜小了")
    else:
        print("猜对了")

print("bye!")