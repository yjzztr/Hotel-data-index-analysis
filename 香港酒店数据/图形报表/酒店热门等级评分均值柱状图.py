import matplotlib.pyplot as plt
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False
# 读入数据
df = pd.read_excel('酒店数据1.xlsx')
# 划分评分等级
df['评分等级'] = pd.cut(df['评分人数'], [0, 2000, 4000, 6000, 8000, 10000, df['评分人数'].max()],
                    labels=['F', 'E', 'D', 'C', 'B', 'A'])
data1 = df['评分等级'].value_counts()
x = data1.index
# 计算均值
MeanF = df.评分[df['评分等级'] == 'F'].mean()
MeanE = df.评分[df['评分等级'] == 'E'].mean()
MeanD = df.评分[df['评分等级'] == 'D'].mean()
MeanC = df.评分[df['评分等级'] == 'C'].mean()
MeanB = df.评分[df['评分等级'] == 'B'].mean()
MeanA = df.评分[df['评分等级'] == 'A'].mean()
df['评分等级'] = pd.cut(df['评分人数'], [0, 2000, 4000, 6000, 8000, 10000, df['评分人数'].max()],
                    labels=[MeanF, MeanE, MeanD, MeanC, MeanB, MeanA])
data2 = df['评分等级'].value_counts()
y = data2.index
# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(x, y, color='r')
plt.title('酒店热门等级评分均值', fontsize=20)
plt.xlabel('热门等级', fontsize=16)
plt.ylabel('评分均值', fontsize=16)
for a, b in zip(x, y):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.show()
