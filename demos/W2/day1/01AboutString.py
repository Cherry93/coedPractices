'''
字符串的处理
'''


# + 连接字符串
# * 子串重复多次形成新的字符串
def operator():
    mstr = "hello" + "world"
    mstr += "!"
    mstr = "coder:" + mstr
    mstr = mstr * 2
    mstr *= 2
    print(mstr)


# 字符串的长度
# 根据下标访问字符串中的字符
def lengthAndChar():
    print(len("hello"))
    print("hello"[0])
    print("hello"[1])
    print("hello"[2])
    print("hello"[3])
    print("hello"[4])
    # 字符串下标越界
    # print("hello"[5])#IndexError: string index out of range


# 字符串子串的截取
def subString():
    mstr = "0123456789"
    print(mstr[5])
    sub = mstr[0:5]  # 含头不含尾
    sub = mstr[0:]  # 一直截取到末尾
    sub = mstr[:5]  # 从头截取
    sub = mstr[:]  # 从头截到尾
    sub = mstr[1:8:2]  # 步长2，每2位截取一位
    sub = mstr[8:1:-2]  # 从后向前截取，每2位截取一位
    print(sub)

# 字符串比较大小
def compareStr():
    # 字符串的大小取决于首字符在字符集中的序号
    # 如果首字符相同，则比较第二个字符，以此类推
    print("1" < "3")
    print("A" < "a")
    print("U000" > "!999")
    print("U000" > "U999")
    print("中国" > "美帝")

# 判断有无子串
def hasChild():
    # find() 有子串则返回【子串首字符的下标位置】，没有子串则返回-1
    # in 判断有无子串，返回布尔值
    # index() 有子串则返回【子串首字符的下标位置】，没有子串则报错：ValueError: substring not found
    print("勇敢的张三".find("张三"))
    print("勇敢的张三".find("张麻子"))
    print("张三" in "勇敢的张三")
    print("张麻子" in "勇敢的张三")
    print("勇敢的张三".index("张三"))
    print("勇敢的张三".index("张麻子"))  # ValueError: substring not found

# 字符串处理函数
def functions1():
    # 格式化字符串
    print("hello world".upper())  # 全大写
    print("HELLO WORLD".lower())  # 全小写
    print("hello world".capitalize())  # 首字母大写
    print("hello world".title())  # 所有单词的首字母大写
    pass

# 字符串处理函数
def functions2():
    # 统计子串次数
    print("谁是张三最爱的人？张三是张三最爱的人".count("张三"))
    print("谁是张三最爱的人？张三是张三最爱的人".count("张三", 3, 11))  # 从下标3-11的范围内寻找
    # 替换子串
    print("张三是张三最爱的人".replace("张三", "李四"))
    print("谁是张三最爱的人？张三是张三最爱的人".replace("张三", "李四", 2))  # 只替换前2处

# 特性判断
def function3():
    print("12345".isdigit())  # 判断是否数字
    print("123hello45".isdigit())
    print("hello".startswith("h"))  # 判断是否以h开头
    print("hello".startswith("hk"))
    print("hello".endswith("lo"))  # 判断是否以lo结尾
    print("hello".endswith("lk"))

# 拆分和重组
def functiion4():
    print("张三-李四-王五".split("-"))  # 以-为分隔符，将字符串炸开为子串的列表：['张三', '李四', '王五']
    print("-".join("hello"))  # 在所有字符之间插入"-":h-e-l-l-o

# 编码和解码
# 编码字符集和解码字符集必须一致，否则会形成乱码
def function5():
    # 使用utf-8字符集，将字符串编码为【字节数组bytes:01010101...】
    print("hello".encode("utf-8"))
    # 将（别处传输过来的）字节数组(bytes),以utf-8为字符集，解码（还原）为字符串
    print(b'hello'.decode("utf-8"))



