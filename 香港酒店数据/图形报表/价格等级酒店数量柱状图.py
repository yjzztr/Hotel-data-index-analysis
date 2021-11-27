import matplotlib.pyplot as plt
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False
# 读入数据
df = pd.read_excel('酒店数据1.xlsx')
# 划分价格等级
df['价格等级'] = pd.cut(df['价格'], [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, df['价格'].max()],
                    labels=['H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'])
data = df['价格等级'].value_counts()
# 设置x，y的值
x = data.index
y = data.values
# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(x, y, color='b')
plt.title('价格等级酒店数量', fontsize=20)
plt.xlabel('价格等级', fontsize=16)
plt.ylabel('酒店数量', fontsize=16)
for a, b in zip(x, y):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.show()
