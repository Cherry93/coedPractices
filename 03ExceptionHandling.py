'''
捕获和处理异常
'''


# 处理某种特定异常
def exceptionHandler1():
    try:
        print("小喇叭开始广播啦")
        print(5 / 0)  # 此处爆发零分母异常，程序跳至异常处理逻辑
        print("此处领取100万")
        print("此处领取1000万")
        print("此处领取一个亿")

    # 捕获和处理零分母异常
    except ZeroDivisionError:
        print("傻鸟，你造了一个零分母异常")
    print("over!")


# 处理多种异常
def exceptionHandler2():
    try:
        print("小喇叭开始广播啦")

        print({"name": "zs"}["age"])
        print([0, 1, 2][100])
        print(5 / 0)

        print("此处领取100万")
        print("此处领取1000万")
        print("此处领取一个亿")

    # 捕获和处理零分母异常
    except ZeroDivisionError:
        print("傻鸟，你造了一个零分母异常")

    # 捕获和处理IndexError
    except IndexError:
        print("傻鸟，你造了下标越界异常")

    # 捕获和处理其它异常
    except:
        print("傻鸟，你造了一个未知的异常")

    print("over!")


# 未发生异常时...
def exceptionHandler3():
    try:
        print("小喇叭开始广播啦")

        # print({"name":"zs"}["age"])
        # print([0,1,2][100])
        # print(5 / 0)

        print("此处领取100万")
        print("此处领取1000万")
        print("此处领取一个亿")

    # 捕获和处理其它异常
    except:
        print("傻鸟，你造了一个未知的异常")

    # 未发生异常时执行的代码
    else:
        print("小伙子干得漂亮，你没有制造任何异常")

    print("over!")


# 无论是否发生异常都执行的代码
def exceptionHandler4():
    try:
        print("小喇叭开始广播啦")

        print({"name": "zs"}["age"])
        # print([0,1,2][100])
        # print(5 / 0)

        print("此处领取100万")
        print("此处领取1000万")
        print("此处领取一个亿")

    # 捕获和处理其它异常
    except:
        print("傻鸟，你造了一个未知的异常")

    # 未发生异常时执行的代码
    else:
        print("小伙子干得漂亮，你没有制造任何异常")

    # 无论是否发生异常都执行的代码
    finally:
        print("生、死、腾讯")

    print("over!")


# 给异常起别名
def exceptionAlias():
    try:
        print([0, 1, 2][100])
        print({"name": "zs"}["age"])
        print(5 / 0)

    # 当发生异常时，系统会创建一个异常类的实例，此处e即为该实例的别名
    except Exception as e:
        print("傻鸟，你造了一个异常：", e, e.__cause__, e.__class__)


exceptionAlias()
