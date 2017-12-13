'''
·封装坏蛋类用以存储坏蛋的信息
·坏蛋拥有人的一切正常属性和功能
·坏蛋讲故事的风格和普通人不一样
·坏蛋有【恶习】属性和【作恶】方法
·创建一个坏蛋，为其设置其基本信息和恶习
·令其作恶
'''

# 封装Person类
class Person:
    # 定义人的属性
    name = "无名氏"
    age = 0

    # 财产为私有属性，外界无法直接访问
    __rmb = 0.00
    __pwd = "111111"

    # 人的构造方法：接收和初始化属性的值
    def __init__(self, name, age, rmb, pwd):
        self.name = name
        self.age = age
        self.__rmb = rmb
        self.__pwd = pwd
        pass

    # 人会讲故事
    def tellStory(self):
        print("我是{0}，我今年{1}岁".format(self.name, self.age))

    # 私有方法，存款查询，外界无法访问
    def __getRmb(self):
        return self.__rmb  # 自己可以访问自己的私有属性

    def getRmb(self):
        pwd = input("叔叔请输入密码：")
        if pwd == self.__pwd:
            return self.__getRmb()  # 自己可以调用自己的私有方法
        else:
            return "fuck off"

# 继承于Person类：即使一行代码都不写，都默认拥有Person的全部属性和方法
class Bastard(Person):

    # 重写（覆写）父类的讲故事方法
    def tellStory(self):
        print("劳资乃{0}，劳资{1}岁".format(self.name, self.age))

    # 特有属性
    badHobby = "未知恶习"

    # 特有方法：作恶
    def doBad(self):
        print("劳资{0}专好{1}".format(self.name,self.badHobby))

    # 拓展父类方法
    def __init__(self, name, age, rmb, pwd,badHobby):

        # 父类方法的原来实现
        # super(Bastard, self).__init__(name,age, rmb, pwd)
        super().__init__(name,age, rmb, pwd)

        # 拓展恶习
        self.badHobby = badHobby
        pass

# 对函数和类进行测试
# 回归测试
# 外界在导入或引用该模块时，回归测试不会自动触发
if __name__ == '__main__':
    b = Bastard("张三",20,123.45,"123456","制造BUG")
    b.tellStory()
    b.doBad()
    pass