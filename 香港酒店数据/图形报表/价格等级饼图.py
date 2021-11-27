import matplotlib.pyplot as plt
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False
# 读取数据
df = pd.read_excel('酒店数据1.xlsx')
# 划分价格等级
df['价格等级'] = pd.cut(df['价格'], [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, df['价格'].max()],
                    labels=['H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'])
data = df['价格等级'].value_counts()
# 设置x,y值
x = data.values
y = x / sum(x)
# 绘制饼图
plt.figure(figsize=(15, 10))
plt.pie(y, labels=data.index, autopct='%.1f %%')
plt.title('价格等级占比')
plt.legend()
plt.show()
