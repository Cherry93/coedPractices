'''
·遍历一个名单
·将最符合有钱、帅炸、勤劳、勇敢、有爱等条件的人找出来
'''

# 列表：候选人名单
mlist = [
    "穷逼、帅炸、懒惰、怂包、有爱的张三",
    "有钱、丑爆、勤劳、怂包、自私的李四",
    "有钱、丑爆、懒惰、怂包、有爱的王五",
    "穷逼、帅炸、勤劳、勇敢、自私的赵六",
    "有钱、丑爆、懒惰、勇敢、有爱的洪七公",
    "有钱、帅炸、勤劳、勇敢、自私的朱重八"
]

# 最佳人选虚位以待
maxScore = 0
theBest = None

# 遍历列表，逐个打分，i=0,1,2,3,4,5
for i in range(0,6,1):

    # 从列表中读取第i个元素
    name = mlist[i]
    # print(name)

    score = 0
    # 统计当前人选得分
    # 从字符串name中寻找"有钱"子串出现的位置
    # 如果没有该子串，则返回-1
    if name.find("有钱") != -1:
        score += 1

    # 名字里带帅炸，加一分
    if name.find("帅炸") != -1:
        score += 1

    # 名字里带勤劳，加一分
    if name.find("勤劳") != -1:
        score += 1

    # 名字里带勇敢，加一分
    if name.find("勇敢") != -1:
        score += 1

    # 名字里带有爱，加一分
    if name.find("有爱") != -1:
        score += 1

    # 打印人选得分
    print("【%s】的得分是%d"%(name,score))

    # 判断当前人选是否优于先前的最佳人选
    # 如果当前人选得分超过已知最高分，则刷新人选
    if score > maxScore:
        maxScore = score
        theBest = name

print("最佳人选是【%s】，他的得分是%d"%(theBest,maxScore))
