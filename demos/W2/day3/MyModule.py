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

# 将自身的业务逻辑（与外界无关）放在回归测试中
# 这样外界在引入当前模块时，当前模块的业务逻辑就不会被触发
if __name__ == '__main__':
    # Person.py的业务逻辑
    p = Person("张三",20,123.45,"123456")
    p.tellStory()