'''
·在创建对象时打印日志
·在对象销毁时打印日志
·自定义对象的打印样式
·设法统计人的“长度”
-----
·实现任意两个人的能力比较
·重载加法运算符，模拟两个人的合作效果
·重载减法运算符，模拟两个人的撕逼内耗效果
'''
from demos.W2.day3.MyModule import Person

class Robot(Person):

    # 构造方法，创建对象时调用
    def __init__(self,name, age, rmb, pwd):
        print("劳资被创建了！")
        super(Robot, self).__init__(name, age, rmb, pwd)

    # 析构函数，释放对象时调用
    def __del__(self):
        # print("劳资被销毁了！")
        pass

    # 返回实例的打印样式
    def __str__(self):
        return "Robot[name:%s;age:%d]"%(self.name,self.age)

    # 自定义实例的“长度”，外界在调用len(obj)触发
    def  __len__(self):
        return 12345

    # 定义两个Robot对象的比较逻辑，用于两个两个Robot对象的比较运算，返回值是布尔值
    # other前来比较的同类对象
    # greater than 的缩写
    def __gt__(self, other):
        return self.age > other.age

    # 定义两个Robot对象的相加逻辑
    def __add__(self, other):
        return Robot(
            self.name+other.name+"组合狗",
            self.age if self.age>other.age else other.age,
            0,"123456"
        )

    # 定义两个Robot对象的减法逻辑
    def __sub__(self, other):
        return Robot("一只猫咪",0,0,None)

r = Robot("贝塔狗", 1, 0.0, "123456")
# r.tellStory()
print(r)#<__main__.Robot object at 0x000001F196F10748>
print("贝塔狗的长度是",len(r))

r1 = Robot("伽马狗", 1, 0.0, "123456")
r2 = Robot("西塔狗", 20, 0.0, "123456")
print("r1 > r2",r1 > r2)#TypeError: '>' not supported between instances of 'Robot' and 'Robot'
print("r1 + r2",r1 + r2)
print("r1 - r2",r1 - r2)