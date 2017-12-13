'''
常见错误
·语法错误
·逻辑错误：业务逻辑错误
·运行时错误：在解释运行时才能暴露出来的错误
'''

# 语法错误
# print("hel，lo)
# print("hello
#       你好")
# print(“”)
# a，b = eval(input("请输入两个值"))

# 逻辑错误
print("半径为3的圆的面积是：",3.14*12345)

# 运行时错误：
# a,b = (input("请输入两个值"))#ValueError: too many values to unpack (expected 2)
# print(5/0)#ZeroDivisionError: division by zero
radius = "20"
area = 3.14 * radius * radius#TypeError: can't multiply sequence by non-int of type 'float'
