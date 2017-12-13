'''

'''
import math


def answer504():
    for i in range(1, 11, 1):
        print("%d公里\t%s英里" % (i, format(1.609 * i, ".3f")))


def answer505():
    # j = 15
    # for i in range(1,200,2):
    #     j += 5
    #     print("%3d公斤\t%10s磅"%(i,format(2.2*i,".1f")),"%10s公斤\t%10d磅"%(format(j/2.2,".2f"),j))=

    j = 15
    for i in range(1, 200, 2):
        j += 5
        print(i, j)


def answer509():
    start = 10000
    growth = 0.05

    money = 0
    for i in range(0, 0 + 4):
        money += start * (1 + growth) ** i
    print("大学四年的学费是%.2f元" % (money))

    money = 0
    for i in range(10, 10 + 4):
        grade = start * (1 + growth) ** i
        money += grade

    print("十年以后大学四年的学费是%.2f元" % money)


def answer515():
    count = 1
    while count ** 3 < 12000:
        ret = count ** 3
        print(ret)
        count += 1
    print("结果是", count - 1)


def answer515X():
    # print(int(12000 ** (1/3)))
    print(math.floor(12000 ** (1 / 3)))
    pass


def answer517():
    start = ord("!")
    end = ord("Z")

    # # 逆序打印
    # for i in range(end,start-1,-1):
    #     print(chr(i))

    for i in range(start, end + 1, 10):
        for j in range(10):
            if (i + j) > end:
                break
            print(chr(i + j), end=" ")
        print("")


answer517()
