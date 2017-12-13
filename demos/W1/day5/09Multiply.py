'''
·以三角的形式打印九九 乘法表
'''

# 外层循环1-9，每次打印一整行
for i in range(1,10):
    # print(i)
    # 内层循环，第ｉ行，打印i次，j从1循环到i
    # i*1=xx i*2=xx ... i*i=xx
    for j in range(1,i+1):
        print("%d*%d=%2d"%(i,j,i*j),end=" ")

    # 每行结束输出一个换行符
    print("",end="\n")
