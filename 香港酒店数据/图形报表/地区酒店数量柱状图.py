import matplotlib.pyplot as plt
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False
# 读取数据
df = pd.read_excel('酒店数据1.xlsx')
data = df['地区'].value_counts()
# 设置x,y的值
x = data.index
y = data.values
# 绘制柱状图
plt.figure(figsize=(16, 10))
plt.bar(x, y, color='r')
plt.title('各个地区酒店数量', fontsize=20)
plt.xlabel('地区', fontsize=16)
plt.ylabel('酒店数量', fontsize=16)
plt.xticks(rotation=90)
for a, b in zip(x, y):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.show()
