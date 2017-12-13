'''

'''

# 定义常量
PI =  3.14

# 定义变量，并反复修改其值
# Python是弱类型语言，一个变量可以赋各种类型的值
radius = 0
radius = 0.0
radius = "0"

# 标识符
aA_1 = 0
# 1aA_1 = 0
def bB_2():
    pass
# def 2bB_2():
#     pass

# 增强型运算符
a = 1
# a = a + 2
# a += 2
# a = a - 2
# a -= 2
# a = a * 2
# a *= 2
# a = a / 2
# a /= 2
# a = a // 2
# a //= 2
# a = a % 2
# a %= 2
# a = a ** 2
# a **= 2
# print(a)

# 内建函数（不必导入外部模块，直接调用的系统函数）
print(type("123"))
print(id("123"))#打印值的地址
a = int("123")
a = int(123.456)
a = float("123")
a = float("123.456")
a = float(123)
a = str(123)
a = str(123.456)
print(a,type(a))

# 转义字符
print("hello\tworld")#制表符
print("hello\nworld")#换行符
print("hello\bworld")#退格
print("helloooooo\rworld")#回车
print("hello\\borld")#反斜线（两个反斜线表示）
print(r"hello\borld")#r=声明字符串中没有转义字符
print("鲁迅：\"人生苦短，请用拍森\"")
print('鲁迅：\'人生苦短，请用拍森\'')
