import random


def answer130105():
    path = input("请输入文档路径：")
    targetWord = input("请输入要删除的字符")
    with open(path, "r+", encoding="utf-8") as file:
        oldText = file.read()
        # newText = oldText.replace(targetWord, "")
        newText = oldText.replace(targetWord, "九")

        file.seek(0)
        file.truncate()

        file.write(newText)
        pass


def answer130304():
    # 生成虚拟数据
    # scoreList = []
    # for i in range(70):
    #     score = random.randint(0,100)
    #     score = str(score)+" "
    #     scoreList.append(score)
    # print(scoreList)
    # path = input("请输入文档路径：")
    # with open(path,"r+",encoding="utf-8") as file:
    #     file.writelines(scoreList)
    path = input("请输入文档路径：")
    with open(path, "r+", encoding="utf-8") as file:
        text = file.read()
        scoreList = text.split(" ")

        # scoreList.sort()
        # tempList = []
        # for scoreStr in scoreList:
        #     tempList.append(int(scoreStr))
        tempList = [int(scoreStr) for scoreStr in scoreList]

        tempList.sort()
        print(tempList)

        total = 0
        for score in scoreList:
            total += int(score)
        print(total)

        print("avg=", total / len(scoreList))

        pass

        # answer1301()

answer130105()