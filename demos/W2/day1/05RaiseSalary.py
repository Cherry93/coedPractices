'''
加薪骗局（局部变量，全局变量，形式参数，实际参数）
·以参数接收加薪前的薪水
·在加薪函数内改变薪水的值
·打印“加薪”后的薪水
---
·实现真正的加薪
'''

'''
@形参和实参
·形式参数：【函数定义】中的参数，叫什么都【无所谓】，且与外界无关
·实际参数：【函数调用】时传递的参数，值是什么【有所谓】
·形参接收的基本类型参数是对实参的拷贝

@局部变量和全局变量
·局部变量：函数参数、定义在函数内的变量——不影响外界
·全局变量：函数以外定义的变量

@函数内的运算结果影响外界的两种方式：
·外界接收函数的返回值
·在函数内声明对全局变量的引用
'''

#
gongzi = 2000#全局变量

def raiseMoney(money):#money=形参，局部变量
    print(money)
    gongzi = 10000#局部变量

    money *= 2

    # 返回局部变量的运算结果
    return money

def raiseMoneyII():
    global gongzi #在函数内声明对全局变量的引用
    gongzi = 5000

raiseMoney(2000)#2000=实参
raiseMoney(gongzi)#形参money对实参gongzi的接收是拷贝式的
gongzi = raiseMoney(gongzi)# 接收函数返回值，使局部变量的运算结果影响外界

raiseMoneyII()
print(gongzi)

