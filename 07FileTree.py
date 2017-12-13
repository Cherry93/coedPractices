'''

'''
import os

dirCount = 0
fileCount = 0

# 打印某文件夹内的所有文件名
def printFileTree(path):

    global dirCount,fileCount

    # 罗列所有的孩子
    files = os.listdir(path)

    # 遍历所有孩子
    for f in files:

        # 打印孩子的完整路径
        fPath = path + "/" + f
        print(fPath)

        # 如果是文件夹，就继续递归打印文件树
        if os.path.isdir(fPath):
            printFileTree(fPath)
            dirCount += 1

        # 否则啥也不干
        else:
            fileCount += 1

printFileTree("E:/Myprojects")
print(dirCount,fileCount)