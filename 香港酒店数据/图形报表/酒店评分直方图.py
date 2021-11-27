import matplotlib.pyplot as plt
import pandas as pd

# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False
# 读取数据
df = pd.read_excel('酒店数据1.xlsx')
# 绘制直方图
plt.figure(figsize=(10, 6))
plt.hist(df['评分'], bins=10, edgecolor='k')
plt.title('酒店评分')
plt.xlabel('评分')
plt.ylabel('数量')
plt.show()
