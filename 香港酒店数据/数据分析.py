import numpy as np
import pandas as pd

# 读取保存好的数据
df = pd.read_excel('酒店数据1.xlsx')
# 查看“评分”的格式
print('评分的格式为：', df['评分'].dtype)
# 对“评分”进行降序排序
print(df.sort_values(by='评分', ascending=False))
# 对“评分”进行升序排序
print(df.sort_values(by='评分', ascending=True))
# 对“价格”进行降序排序
print(df.sort_values(by='价格', ascending=False))
# 对“价格”进行升序排序
print(df.sort_values(by='价格', ascending=True))
# 计算“油尖旺”地区的均价
print('油尖旺地区的均价为：', df.价格[df['地区'] == '油尖旺'].mean())
# 对酒店数据进行描述性统计
print('酒店数据的描述性统计如下：', df.describe())
# 酒店价格的描述性统计
print(df['价格'].describe())
print('价格的均值为：', np.mean(df.价格))
print('价格的方差为：', np.var(df.价格))
print('价格的最大值为：', np.max(df.价格))
print('价格的最小值为：', np.min(df.价格))
print('价格的中值为：', np.median(df.价格))
# 评分和价格之间的的相关系数
print('价格与评分的相关系数为：', df[['价格', '评分']].corr())
# 评分和价格之间的的协方差
print('价格与评分的协方差为：', df[['价格', '评分']].cov())
# 按照评分降序排序，评分相同时按价格升序排序
print(df.sort_values(by=['评分', '价格'], ascending=(True, False)))
# 评分小于3分的酒店数量
print('评分小于3的酒店数量：', np.sum(df.评分 < 3))
# 评分小于3分的酒店的占比
print('评分小于3的酒店数量占比: {:.2%}'.format(np.sum(df.评分 < 3) / np.sum(df.评分)))
# 酒店评分大于等于4分的酒店的价格均值
print('评分大于等于4的酒店价格均值为：', np.mean(df.价格[df['评分'] >= 4]))
# 计算出每个地区的酒店占总酒店数量的比例
print('每个地区的酒店数量：', df['地区'].value_counts())
print('该地区酒店占总酒店数量的比例：', df['地区'].value_counts() / len(df))
# 找出酒店评分人数排名前20的酒店，并计算他们的价格均值
df.sort_values(by='评分人数', ascending=False, inplace=True)
print('评分人数排名前20的酒店是：', df[:20])
print('评分人数排名前20的酒店均价为：', df.价格[:20].mean())
# 酒店分布的类型数量
print('酒店的类型有：', df['类型'].unique())
print('酒店的类型数量有：', len(df['类型'].unique()))
# 酒店分布的地区数量
print('酒店的分布地区有：', df['地区'].unique())
print('酒店分布地区的数量有：', len(df['地区'].unique()))
# 统计各个类型和地区包含的酒店数量
print(df['地区'].value_counts())
print(df['类型'].value_counts())
