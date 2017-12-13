'''
·随机生成颜值
·如果颜值超过90，输出“恭喜，您的颜值简直逆天”
-----
·否则输出“呵呵，您的颜值很亲民”
-----
·如果超过90，输出“恭喜，您的颜值简直逆天”
·60~90，输出“呵呵，您的颜值很亲民”
·否则输出“我们聊天气吧”
'''
import random

looking = random.randint(0,100)
print(looking)

#1.0 单分支
# if looking > 90:
#     print("恭喜，您的颜值简直逆天")

#2.0 双分支
# if looking > 90:
#     print("恭喜，您的颜值简直逆天")
# else:
#     print("呵呵，您的颜值很亲民")

#3.0 多分支
if looking >= 80:
    pass#占茅坑表达式
    print("恭喜，您的颜值简直逆天")
elif looking>=60 and looking<80:
    pass
    print("您的颜值很亲民")
elif looking>=40 and looking<60:
    pass
    print("您的颜值过得去")
else:
    pass
    print("我们聊聊拍森吧")