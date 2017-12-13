'''
·封装一个“内容丰富”的表白函数
·多次调用之，体会封装后的便利性
-----
·扩展1.0函数
·增加“发件人”，“收件人”参数
·增加“回复”返回值
-----
·扩展2.0
·增加【位置参数】【日期】
·增加【关键字参数】【城市】、【区域】参数
'''

def sayLove():
    print("我是穿过枪林弹雨去睡你")
    print("我是穿过大半个中国去睡你")
    print("我是把无数黑夜摁进一个黎明去睡你")
    print("我是无数个我奔跑成一个我去睡你")

'''
toWhom 收信人
sender 发信人
返回值 表白的结果
'''
def sayLoveX(toWhom,sender,count):
    print("亲爱的%s:"%(toWhom))
    print("我是穿过枪林弹雨去睡你")
    print("我是穿过大半个中国去睡你")
    print("我是把无数黑夜摁进一个黎明去睡你")
    print("我是无数个我奔跑成一个我去睡你")
    print("爱你%d年的%s"%(count,sender))

'''
toWhom,sender,count
位置参数 没有默认值 必填 次序不能变

city="深圳",area="宝安" 键值对形式
关键字参数 有默认值 非必填 次序可以打乱（如果保持原有次序，可以不写键）
'''
def sayLoveXX(toWhom,sender,count,city="深圳",area="宝安"):
    print("亲爱的%s:"%(toWhom))
    print("我是穿过枪林弹雨去睡你")
    print("我是穿过大半个中国去睡你")
    print("我是把无数黑夜摁进一个黎明去睡你")
    print("我是无数个我奔跑成一个我去睡你")
    print("爱你%d年的%s"%(count,sender))
    print("于%s,%s"%(city,area))

    return "哦"

# sayLoveX("凤凤","郭小明")

# result = sayLoveX("如花","郭小明",10000)
# print("对方的回复是：",result)

# result = sayLoveXX("如花","郭小明",10000,area="二院")
# result = sayLoveXX("如花","郭小明",10000,city="广州",area="二院")
# result = sayLoveXX("如花","郭小明",10000,area="二院",city="广州")
# result = sayLoveXX("如花","郭小明",10000,"广州","二院")
# print("对方的回复是：",result)

def register(name,isMan,age,home="江西",rmb=0.0):
    print("姓名：",name)
    print("性别：","男" if isMan==True else "女")
    print("年龄：",age)
    print("家乡：",home)
    print("资产：",rmb)

# register("张三",True,20,home="广东",rmb=123.45)
register("张三",True,20,rmb=123.45,home="广东")
# register("张三",True,20,"广东",123.45)
