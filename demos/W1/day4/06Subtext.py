'''
·我不想破坏我们之间的友谊=？；
·你真是一个好人=？
·我们还是做朋友好了=？
·给我一段时间考虑=？
·我有男友了=？
·我还没有勇气接受你=？
·我爸妈不让我谈恋爱=？
·~=我们还没有收录
'''

text = input("女神对你说：")
subtext = None  # 潜台词初始值为空

if text == "我不想破坏我们之间的友谊":
    subtext = "我们之间也只存在友谊"
elif text == "你真是一个好人":
    subtext = "还没有好到我能接受的程度"
elif text == "我们还是做朋友好了":
    subtext = "我们也只能是朋友"
elif text == "给我一段时间考虑":
    subtext = "没时间怎么开溜"
elif text == "我有男友了":
    subtext = "你不如我男朋友"
elif text == "我还没有勇气接受你":
    subtext = "看见你差点被吓死"
elif text == "我爸妈不让我谈恋爱":
    subtext = "爸妈不让我和你谈恋爱"
else:
    subtext = "该款机器人暂未收录"

print("女神的潜台词是%s" % subtext)
