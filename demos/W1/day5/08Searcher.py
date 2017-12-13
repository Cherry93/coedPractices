'''
·输入女神名字
·遍历一个名单，找到女神就结束遍历
·名单中带“（保护）”字样的，不对外提供查询服务，碰到就跳过去
'''

mlist = ["范冰冰","饭岛爱","范否（保护）","饭没了秀","范仲淹","范志毅","范伟","范玮琪"]
name = input("请输入你丢失的女神：")

found = False
for i in range(0,len(mlist)):
    item = mlist[i]

    # 跳过受保护的人员
    if item.find("（保护）")!=-1:
        continue

    print(item)
    if item == name:
        print("已找到，您丢失的女神【%s】位于我院第%d号床位"%(name,i))
        found = True
        break

if found == False:
    print("没有找到")