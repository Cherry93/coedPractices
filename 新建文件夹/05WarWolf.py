'''
·为帝国创建一支军队，包含骑兵、弓箭手、法师
·所有兵种都能够进攻和防守，但形态各异
·通过输入将令，控制每个兵种的攻守细节
'''

# 战士父类
class Fighter:
    def attack(self):
        print("拳打脚踢")

    def defend(self):
        print("抱紧脑袋")

# 战士子类：骑兵
class Rider(Fighter):
    def attack(self):
        print("同志们，冲啊")

# 战士子类：法师
class Master(Fighter):
    def attack(self):
        print("天灵灵地灵灵，云中飞来百万兵")

# 战士子类：弓箭手
class Archer(Fighter):
    def attack(self):
        print("我的三分剑，是地狱的火焰")


def sendOrder():
    #
    cmd = input("将军请传将令")
    # 调度全体
    if cmd == "99":
        # 全体进攻（共性）
        for fighter in fighters:
            fighter.attack()
    elif cmd == "90":
        # 全体进攻（共性）
        for fighter in fighters:
            fighter.defend()

    # 调度骑兵
    elif cmd == "19":
        # 遍历所有战士实例
        for fighter in fighters:

            # 判断当前实例是否是骑兵实例
            if isinstance(fighter, Rider) == True:
                fighter.attack()

    elif cmd == "10":
        # 遍历所有战士实例
        for fighter in fighters:

            # 判断当前实例是否是骑兵实例
            if isinstance(fighter, Rider):
                fighter.defend()

    # 调度法师
    elif cmd == "29":
        pass
    elif cmd == "20":
        pass

    # 调度弓箭手
    elif cmd == "39":
        pass
    elif cmd == "30":
        pass


if __name__ == '__main__':

    # 军队者，一堆战士也
    r = Rider()
    m = Master()
    a = Archer()
    fighters = [r,m,a]

    while True:
        sendOrder()
