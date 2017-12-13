'''
·为存款信息添加保护，使其不能被直接访问
·增加设置密码功能
·增加存款查询功能，只有输入密码正确的情况下才能查询存款信息
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
        print("我是{0}，我今年{1}岁，我的财产是{2}元".format(self.name, self.age, self.__rmb))

    # 私有方法，存款查询，外界无法访问
    def __getRmb(self):
        return self.__rmb  # 自己可以访问自己的私有属性

    def getRmb(self):
        pwd = input("叔叔请输入密码：")
        if pwd == self.__pwd:
            return self.__getRmb()  # 自己可以调用自己的私有方法
        else:
            return "fuck off"


# 使用类的构造方法，创建Person的实例，并初始化其属性
p1 = Person("张三", 20, 100.00, "idontknow")

# print(p1.__rmb)#私有属性无法直接访问
# print(p1.__getRmb())#私有方法无法直接调用

# 通过公开方法（有条件地）访问私有属性
print(p1.getRmb())
