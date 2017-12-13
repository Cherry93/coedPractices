'''
·扩展3.0
·增加【不定长位置参数】【点赞者】
·增加不定长关键字参数【备注信息】
·可选顺序：
    √定长位置，不定长位置，定长关键字，不定长关键字（推荐顺序）
    √定长位置，定长关键字，不定长位置，不定长关键字
'''

'''
*likesBy 不定长位置参数 （元组） 接收任意多个值（0到无穷）
**infos 不定长关键字参数 {字典} 接收任意多个键值对
'''


def sayLoveXXX(
        toWhom, sender,  # （定长）位置参数
        *likesBy,  # 不定长位置参数
        city="深圳", area="宝安",  # （定长）关键字参数
        **infos  # 不定长关键字参数
):
    print("亲爱的%s:" % (toWhom))
    print("我是穿过枪林弹雨去睡你")
    print("我是穿过大半个中国去睡你")
    print("我是把无数黑夜摁进一个黎明去睡你")
    print("我是无数个我奔跑成一个我去睡你")
    print("爱你的%s" % (sender))
    print("于%s,%s" % (city, area))
    print("以下人等纷纷点赞:", likesBy)
    print("-----")
    print("以下是备注信息：", infos)

    return "哦"


def register(
        name,
        *familyMember,
        #-----推荐参数定义顺序：先位置，再关键-----
        age=0, nickname="john smith",
        **infos
):
    print(name)
    print(familyMember)
    print(age,nickname)
    print(infos)


# sayLoveXXX("凤凤","郭明明","如花","阿珍","包租婆","酱爆",area="福田")
# sayLoveXXX("凤凤","郭明明",area="福田")
# sayLoveXXX(
#     "凤凤","郭明明",
#     "如花","阿珍","包租婆","酱爆",
#     city="深圳",area="福田",
#     time="15:18",food="鸡翅",drink="可乐"
# )

# sayLoveIV(
#     "凤凤","小四",
#     "广州","福田",
#     "如花","阿珍","包租婆","酱爆",
#     time="15:18",food="鸡翅",drink="可乐"
# )

def sayLoveIV(
        toWhom, sender,  # （定长）位置参数
        city="深圳", area="宝安",  # （定长）关键字参数
        *likesBy,  # 不定长位置参数
        **infos  # 不定长关键字参数
):
    print("亲爱的%s:" % (toWhom))
    print("我是穿过枪林弹雨去睡你")
    print("我是穿过大半个中国去睡你")
    print("我是把无数黑夜摁进一个黎明去睡你")
    print("我是无数个我奔跑成一个我去睡你")
    print("爱你的%s" % (sender))
    print("于%s,%s" % (city, area))
    print("以下人等纷纷点赞:", likesBy)
    print("-----")
    print("以下是备注信息：", infos)

    return "哦"

register(
    "jack",
    "fuck","shit","ass",
    age=12,nickname="bill",
    food="鸡腿",drink="啤酒"
)
