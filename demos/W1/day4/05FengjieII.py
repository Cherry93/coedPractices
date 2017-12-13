'''
·回答是否有钱
·如果有钱，进入下一轮判断，否则出局
·有钱的情况下，如果帅炸，凤姐就从了你，否则出局
'''

rich = input("有钱吗？Y/N")
if rich == "Y":
    # 第二轮
    print("恭喜你进入第二轮...")
    handsome = input("帅炸吗？Y/N")
    if handsome=="Y":
        print("恭喜你，抱得凤姐归")
    else:
        print("fuck off!")
else:
    print("fuck off!")