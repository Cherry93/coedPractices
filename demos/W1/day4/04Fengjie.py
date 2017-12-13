'''
·回答是否有钱、是否帅炸
·如果有钱且帅炸，凤姐就从了你
·如果有钱或帅炸，我们还是做朋友好了
·如果没钱还丑，有多远滚多远
'''
rich = input("有钱吗？Y/N")
handsome = input("帅炸吗？Y/N")

if rich=="Y" and handsome=="Y":
    print("凤姐就从了你")
    pass
elif rich=="Y" or handsome=="Y":
    print("你成为凤姐的朋（bei）友（tai）")
    pass
else:
    print("有多远滚多远！")
    pass