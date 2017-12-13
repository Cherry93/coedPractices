'''
条件表达式拾遗
'''

# 逻辑运算符
# if not ((1+1)==2):
#     print("成立")
# else:
#     print("不成立")

# 比较运算符的结果是布尔值
# ret1 = ((1+1) ==2)
# ret2 = ((1+1) < 3)
# print(ret1,ret2)
#
# # 逻辑运算符的结果是布尔值
# print(True and True)
# print(True and False)
# print(False and False)
# print(True or True)
# print(True or False)
# print(False or False)
# print(not True)
# print(not False)

# 条件表达式
a = False
a = 0
a = 0.0
a = None
a = ""

# 其余都成立
a = True
a = 123
a = -123
a = 5.0
a = "hello"

if a:
    print("成立")
else:
 print("不成立")

# 条件推导式
# value = "a" if (True) else "b"
amIHandsome = "帅呆了" if((1+1)==3) else "丑爆了"
amIHandsome = 1 if(None) else 0
amIHandsome = False if(not 5) else True
print(amIHandsome)

# True与1相等，Faslse与0相等
print(True == 1)
print(False == 0)