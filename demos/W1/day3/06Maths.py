'''
一只数学家
·加减乘除
·整除、求余
·求绝对值、最大值、最小值
·四舍五入、下舍、上入
·求角度的正弦、余弦、正切
·角度、弧度互转
·乘方和开方
·求对数
·求三角函数
'''
import math

print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)

print(10 // 3)  # 整除 3
print(10 % 3)  # 求余（取模） 1

# 求绝对值、最大值、最小值
print(abs(-5))
print(math.fabs(-5))
print(max(3, 4, 7))
print(min(3, 4, 7))

# 四舍五入、下舍、上入
print(round(3.4))  # 四舍五入3
print(round(3.5))  # 四舍五入4
print(math.floor(3.9))  # 下舍=3
print(math.ceil(3.1))  # 上入=4

# 角度、弧度互转
print(math.degrees(3.141592653589793))  # 弧度转换为角度
print(math.degrees(math.pi))  # 弧度转换为角度
print(math.radians(180))  # 角度转换为弧度

# 乘方和开方
print(math.pow(2,3))
print(2 ** 3)
print(math.sqrt(9))#9的开方
print(8 ** (1/3))#给8开3次方s

# 求对数
print(math.log(8,2))#计算以2位底，8的对数，=3
print(math.log(100))#默认底数为自然对数math.e
print(math.log10(100))#计算以10位底，100的对数，=2

# 算术运算的优先级：括>幂>乘>加
result = 1 + 2 * 3 ** (4-2)
print(result)

# 三角函数(角度参数必须以弧度表示)
mAngle = math.radians(30)
print(math.sin(mAngle))
print(math.cos(mAngle))
print(math.tan(mAngle))