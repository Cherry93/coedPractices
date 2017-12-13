'''
·扩展4.0
·令函数有多个返回值，且返回值类型不一
'''

def sayLove():
    print("我是穿过枪林弹雨去睡你")
    print("我是穿过大半个中国去睡你")
    print("我是把无数黑夜摁进一个黎明去睡你")
    print("我是无数个我奔跑成一个我去睡你")

    # 一次返回多个返回值
    return "哦",666,False

# 接收函数的返回值，如果是多个，则其类型是元组
result = sayLove()
print(result)