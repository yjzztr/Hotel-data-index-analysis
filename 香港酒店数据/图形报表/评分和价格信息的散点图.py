import matplotlib.pyplot as plt
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False
# 读取数据
df = pd.read_excel('酒店数据1.xlsx')
# 设置x,y的值
x = df['评分']
y = df['价格']
# 绘制散点图
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='c', marker='p')
plt.title('酒店评分和价格', fontsize=20)
plt.xlabel('评分', fontsize=16)
plt.ylabel('价格', fontsize=16)
plt.show()
