'''
·封装男人类，继承于Person，使之有阳刚风格的自我介绍，使之能咆哮
·封装女人类，继承于Person，使之有阴柔风格的自我介绍，使之能撒娇
·封装Gay类，使之同时具有男人和女人的特性
·令其咆哮，令其撒娇
·令其偏阳刚地进行自我介绍，令其偏阴柔地进行自我介绍
'''
from demos.W2.day3.MyModule import Person

class Man(Person):
    def tellStory(self):
        print("朕乃{0}，朕今年{1}岁了".format(self.name, self.age))

    def roar(self):
        print("%s:劳资天下第一"%(self.name))

class Woman(Person):
    def tellStory(self):
        print("伦家乃{0}，伦家今年{1}岁了".format(self.name, self.age))

    def sajiao(self):
        print("%s:好讨厌了啦"%(self.name))

# 小攻
class AttackingGay(Man, Woman):
    pass

# 小受
class DefendingGay(Woman,Man):
    pass

if __name__ == '__main__':
    # m = Man("张三", 20, 123.45, "123456")
    # m.tellStory()
    # m.roar()
    # wm = Woman("翠花", 20, 123.45, "123456")
    # wm.tellStory()
    # wm.sajiao()

    g = AttackingGay("东方不败", 20, 123.45, "123456")
    g.roar()
    g.sajiao()
    g.tellStory()#小攻优先继承Man的tellStory()

    print("\n")
    g = DefendingGay("西方失败", 20, 123.45, "123456")
    g.roar()
    g.sajiao()
    g.tellStory()#小受优先继承Woman的tellStory()



