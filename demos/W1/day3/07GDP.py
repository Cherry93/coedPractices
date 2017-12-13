'''
·求天朝和美帝10年后的GDP
'''

# 驼峰风格的变量命名
# 天朝和美帝2017年GDP（万亿美元）
usGdp = 18.36
cnGdp = 11.72

# # 下划线风格的变量命名
# us_gdp = 18
# cn_gdp = 11

# 年增长率（百分点）
usGrowth = 2
cnGrowth = 6.5

print("天朝10年以后GDP", cnGdp * ((100 + cnGrowth) / 100) ** 10)
print("美帝10年以后GDP", usGdp * ((100 + usGrowth) / 100) ** 10)
