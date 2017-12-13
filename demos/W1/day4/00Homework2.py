'''
·求当前时间距离1970年0时逝去了多少秒
·求当前时间距离1970年0时逝去了多少分钟
·求当前时间距离1970年0时逝去了多少小时
·求当前时间距离1970年0时逝去了多少天
·求当前时间距离1970年0时逝去了多少年
·求当前时分秒
'''
import time

# 求当前时间距离1970年0时逝去了多少秒
seconds = int(time.time())
print(seconds)

# 求当前时间距离1970年0时逝去了多少分钟
minutes = seconds // 60
print(minutes)

# ·求当前时间距离1970年0时逝去了多少小时
hours = seconds // (60*60)
print(hours)

# ·求当前时间距离1970年0时逝去了多少天
days = seconds // (60*60*24)
print(days)

# ·求当前时间距离1970年0时逝去了多少年
years = seconds // (60*60*24*365)
print(years)

# ·求当前时分秒
todaySeconds = seconds % (60*60*24)
timeHours = todaySeconds // 3600 + 8
timeMinutes = todaySeconds % 3600 // 60
timeSeconds = todaySeconds % 60
# print(timeHours,timeMinutes,timeSeconds)
# print("当前时间：",timeHours,":",timeMinutes,":",timeSeconds)
print("当前时间：%d:%d:%d"%(timeHours,timeMinutes,timeSeconds))


