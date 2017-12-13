class Person:

    name = "无名氏"
    age = 0
    __rmb = 123

    def __init__(self):
        print("劳资被创建了")

    # 实例方法
    # 通过实例去调用
    def instanceMethod(self):
        print("instanceFunc")

    # 在方法的头顶添加静态方法装饰器，代表die是一个静态方法
    # 静态方法：通过类去调用，无需创建对象
    # 静态方法相当于写在类的作用域中的普通方法
    @staticmethod
    def die():
        print("%s腿一蹬，眼一闭"%(Person.name))

    # 在方法的头顶添加类方法装饰器，代表当前是一个类方法
    # cls = 当前类，可以通过cls访问当前类中的所有属性和方法，还可以通过cls创建当前类的实例
    @classmethod
    def cMethod(cls):
        print(cls.name)
        print(cls.age)
        print(cls.__rmb)
        cls.die()
        obj = cls()





if __name__ == '__main__':
    # 实例方法，通过实例去调用
    mc = Person()
    mc.instanceMethod()
    mc.cMethod()

    # 静态方法：纯粹只是写在类中的普通方法
    mc.die()
    Person.die()

    # 类方法：可以访问类的信息、创建类的实例
    Person.cMethod()
    pass