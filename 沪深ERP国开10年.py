import matplotlib.pyplot as plt
import pandas as pd

# 读取Excel数据
df = pd.read_excel(r'C:\Users\LeslieXiao\Desktop\PyCase_3.xlsx')

# 设置字体和分辨率
plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 获取数据
x1 = df['日期']
y1 = df['沪深ERP']
y2 = df['国开:10年']

# 绘制第一条线
plt.plot(x1, y1, color='grey', label='沪深')
plt.legend(loc='upper left', fontsize=8)

# 添加第二个y轴
plt.twinx()

# 绘制第二条线
plt.plot(x1, y2, color='black', linewidth=1, linestyle='--', label='国开:10年')
plt.legend(loc='upper right', fontsize=8)

# 显示图形
plt.show()