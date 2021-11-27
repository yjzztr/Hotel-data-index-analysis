import numpy as np
import pandas as pd

# 读取数据
df = pd.read_excel('./香港酒店数据.xlsx')
print(df.head())
# 重新设置数据的索引
df.columns = ['索引', '名字', '类型', '城市', '地区', '地点', '评分', '评分人数', '价格']
print(df.head())
# 查找出所有类型为“休闲度假”并且在湾仔地区的酒店
print(df[(df['类型'] == '休闲度假') & (df['地区'] == '湾仔')])
# 查找出所有地址在观塘或者油尖旺，评分大于4的酒店
print(df[(df['地区'] == '观塘') | (df.地区 == '油尖旺') & (df['评分'] > 4)])
# 对缺失数据进行处理
# 找出缺失值
print(df[df['地区'].isnull()])
print(df[df['类型'].isnull()])
print(df[df['评分'].isnull()])
# 用“其他”填充类型和地区
df['地区'].fillna('其他', inplace=True)
print(df[df['地区'].isnull()])
df['类型'].fillna('其他', inplace=True)
print(df[df['类型'].isnull()])
# 用评分均值填充评分缺失值
df['评分'].fillna(np.mean(df['评分']), inplace=True)
print(df[df['评分'].isnull()])
# 删除价格和评分人数的缺失值
df.dropna(subset=['价格', '评分人数'], inplace=True)
# 删除空行
df.dropna(how='all', inplace=True)
# 保存处理好的数据到酒店数据1.xlsx
df.to_excel('./酒店数据1.xlsx')
