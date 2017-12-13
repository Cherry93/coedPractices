'''
·永无休止地输出“我爱XX”一直到死
·每隔一秒输出“我爱XX”一直到死
------
·我爱XX”输出100遍，结束循环
'''
import time

def endlessLove():
    # 反复判断条件是否成立，只要条件成立，就执行循环体
    # 否则就结束循环，继续向后执行
    while 1 + 1 == 2:

        # ---循环体开始---
        print("我爱拉芳")
        print("我爱潘婷")
        time.sleep(1)
        # ---循环体结束---

    print("我爱老婆")

count = 0
# 动态修改循环条件的值
while count < 10:
    print("我爱拉芳")
    time.sleep(1)
    count += 1#count自加1

print("我爱老婆")