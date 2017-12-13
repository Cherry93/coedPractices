'''
接收劳资的输入
·接收圆的半径，输出其面积
'''

'''
20 类型int 整数型
3.14 类型float 浮点型
"20" 类型str 字符串
'''

# 认识基本数据类型
print("20的类型为",type(20))#int
print("3.14的类型为",type(3.14))#float
print("hello的类型为",type("20"))#str

# 使用input函数接收用户的输入，输入的值一定是str类型
radius = input("请输入圆的半径")
print("radius的值为",radius)
print("用户输入的radius类型为",type(radius))

# 使用eval函数对radius进行类型转换，将转换的结果重新赋值给自己
radius = eval(radius)
print("eval转换后radius的类型",type(radius))

# 计算圆的面积
area = 0
area = 3.14 * radius * radius

# 打印结果
print("圆的面积是",area)
