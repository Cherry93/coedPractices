'''
·求当前时间距离1970年0时逝去了多少秒
·求当前时间距离1970年0时逝去了多少分钟
·求当前时间距离1970年0时逝去了多少小时
·求当前时间距离1970年0时逝去了多少天
·求当前时间距离1970年0时逝去了多少年
·求当前时分秒
'''
import time

# 当前距离1970年0时逝去的时间秒数，float
seconds = time.time()

# 将seconds强转为int类型
seconds = int(seconds)

print(seconds)
