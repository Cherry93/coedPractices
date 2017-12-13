'''
·封装字符生成器工具，实现如下功能：
·随机获取小写字母
·随机获取大写字母
·随机获取数字字符
·随机获取ASCII字符
·在外界导入并使用该工具
'''
import random

# 在指定的起止范围内随机获取字符
def getRandomChar(startChar,endChar):
    start = ord(startChar)
    end = ord(endChar)
    randOrd = random.randint(start,end)
    return chr(randOrd)

# 随机获取小写字母
def getRandomLowercase():
    return getRandomChar("a","z")

# 获取随机大写字母
def getRandomUppercase():
    return getRandomChar("A", "Z")

# 获取随机数字
def getRandomNumber():
    return getRandomChar("0", "9")

# print(getRandomUppercase())
# print(getRandomLowercase())
# print(getRandomNumber())