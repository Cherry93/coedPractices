'''
列表
'''


# 认识列表，通过下标访问列表元素
def func1():
    mlist = ["fuck", "shit", "asshole"]
    print(len(mlist))  # 打印列表长度（元素个数）
    print(mlist[0])
    print(mlist[1])
    print(mlist[2])


# 使用for循环遍历列表
def func2():
    mlist = ["fuck", "shit", "asshole"]
    for i in range(0, 3):
        print(mlist[i])


# 寻找字符串子串
def func3():
    mstr = "0123456789"
    print(mstr.find("hello"))  # 没有子串hello，返回-1
    print(mstr.find("456"))  # 有456子串，返回子串首字符的位置下标
    print(mstr.find("4569"))  # 没有子串4569，返回-1


#  遍历过程中，动态寻找最大值
def func4():
    maxNum = -1

    mlist = [3, 1, 4, 1, 5, 9, 2, 6]  # 长度为8
    # 从0循环到7
    for i in range(len(mlist)):
        num = mlist[i]
        # print(num)
        if num > maxNum:
            maxNum = num
    print(maxNum)


# func2()
# func3()
func4()
