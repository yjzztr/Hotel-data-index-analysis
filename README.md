# 项目：酒店数据分析



## 1、项目概述

​	**1.1 项目目标和主要内容**

​		1）掌握 Python 的 pandas, numpy, matplotlib 库，并用其对给定数据进行处理。  

​		2）能够对 excel 的数据进行处理，并加以运算，并根据一定的要求来构造所需的图形报表。

​	**1.2 项目的主要功能**

​		1）能够对给定的 excel 数据进行处理与运算，或对缺省的数据按要求补齐，得到全新的表格。  

​		2）根据新得到的表格能够对构造所需的图形报表。

***

## **2、项目设计**

​		**2.1 系统详细设计**  

​			**2.2.1 数据预处理.py**  

​					1）读取数据

~~~python
df = pd.read_excel('./香港酒店数据.xlsx')
~~~

​					2）对缺省值填充

~~~python
# 用“其他”填充类型和地区
df['地区'].fillna('其他', inplace=True)
print(df[df['地区'].isnull()])
df['类型'].fillna('其他', inplace=True)
print(df[df['类型'].isnull()])
# 用评分均值填充评分缺失值
df['评分'].fillna(np.mean(df['评分']), inplace=True)
~~~

​					3）另存数据

~~~python
df.to_excel('./酒店数据1.xlsx')
~~~

***

​			**2.2.2 数据分析.py**  

​					1）读取数据

~~~python
df = pd.read_excel('酒店数据1.xlsx')
~~~

​					2）升降序排序

~~~python
# 对“评分”进行降序排序
print(df.sort_values(by='评分', ascending=False))
# 对“评分”进行升序排序
print(df.sort_values(by='评分', ascending=True))
# 对“价格”进行降序排序
print(df.sort_values(by='价格', ascending=False))
# 对“价格”进行升序排序
print(df.sort_values(by='价格', ascending=True))
~~~

​					3）描述性统计

~~~python
# 对酒店数据进行描述性统计
print('酒店数据的描述性统计如下：', df.describe())
# 酒店价格的描述性统计
print(df['价格'].describe())
~~~

***

​			**2.2.3 图形报表**  

~~~python
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决负号无法显示问题
plt.rcParams['axes.unicode_minus'] = False
# 读取数据
df = pd.read_excel('酒店数据1.xlsx')
~~~

​					1. 柱状图

​							1）设置 x, y 值  

~~~python
x = data.index
y = data.values
~~~

​							2）绘制柱状图

~~~python
plt.figure(figsize=(16, 10))
plt.bar(x, y, color='r')
plt.title('各个地区酒店数量', fontsize=20)
plt.xlabel('地区', fontsize=16)
plt.ylabel('酒店数量', fontsize=16)
plt.xticks(rotation=90)
for a, b in zip(x, y):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.show()
~~~

​					2. 饼图

​							1）设置等级

~~~python
df['价格等级'] = pd.cut(df['价格'], [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, df['价格'].max()],
                    labels=['H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'])
~~~

​							2）设置 x, y 值

~~~python
x = data.values
y = x / sum(x)
~~~

​							3）绘制饼状图

~~~python
plt.figure(figsize=(15, 10))
plt.pie(y, labels=data.index, autopct='%.1f %%')
plt.title('价格等级占比')
plt.legend()
plt.show()
~~~

 					3. 直方图

​							1）绘制直方图

~~~python
plt.figure(figsize=(10, 6))
plt.hist(df['评分'], bins=10, edgecolor='k')
plt.title('酒店评分')
plt.xlabel('评分')
plt.ylabel('数量')
plt.show()
~~~

 					4. 散点图

​							1）设置 x, y 值

~~~python
x = df['评分']
y = df['价格']
~~~

​							2）绘制散点图

~~~python
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='c', marker='p')
plt.title('酒店评分和价格', fontsize=20)
plt.xlabel('评分', fontsize=16)
plt.ylabel('价格', fontsize=16)
plt.show()
~~~

***

## **3、程序运行结果分析**

1） 数据预处理结果

![数据预处理](D:\Project\Pycharm\python作业\截图\数据预处理.png)

***

2） 数据分析结果

<img src="D:\Project\Pycharm\python作业\截图\数据分析结果.png" alt="数据分析结果" style="zoom:60%;" />

***

3） 各个图表运行结果

![价格等级酒店数量柱状图](D:\Project\Pycharm\python作业\截图\价格等级酒店数量柱状图.png)

![价格等级饼图](D:\Project\Pycharm\python作业\截图\价格等级饼状图.png)

![地方酒店数量柱状图](D:\Project\Pycharm\python作业\截图\地方酒店数量柱状图.png)

![评分和价格信息的散点图](D:\Project\Pycharm\python作业\截图\评分和价格信息的散点图.png)

![酒店热门等级评分均值柱状图](D:\Project\Pycharm\python作业\截图\酒店热门等级评分均值柱状图.png)

![酒店评分直方图](D:\Project\Pycharm\python作业\截图\酒店评分直方图.png)

***

## **4、总结**

​		**4.1 项目的难点与关键点**  

			  1. 初次学习 pandas, numpy, matplotlib 库的使用，对其中的函数不熟悉，运用不够灵活。
			  1.  对函数的参数没有清晰地认识。

​		**4.2 心得体会**  

​			   函数的使用大同小异，熟练掌握其运用方法能很快的完成该项目，学习应融汇贯通，学会灵活使用。
