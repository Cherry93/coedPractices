'''
·封装Person类
·封装以下属性：姓名、年龄、存款
·封装自我介绍方法，陈述以上属性
·创建一个人，设置其基本信息
·打印此人信息
·令此人进行自我介绍
'''

# 封装Person类
class Person:

    # 定义人的属性
    name = "无名氏"
    age = 0
    rmb = 0.00

    # 人的构造方法：接收和初始化属性的值
    def __init__(self, name, age, rmb):
        self.name = name
        self.age = age
        self.rmb = rmb
        pass

    # 人会讲故事
    def tellStory(self):
        print("我是{0}，我今年{1}岁，我的财产是{2}元".format(self.name,self.age,self.rmb))

# 使用类的构造方法，创建Person的实例，并初始化其属性
p1 = Person("张三",20,100.00)
p2 = Person("李四",30,200.00)

# 让这两个实例讲故事
p1.tellStory()
p2.tellStory()