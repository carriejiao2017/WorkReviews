# import matplotlib. pyplot as plt
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth = 5)
# plt.title(" Square Numbers", fontsize= 24)
# plt.xlabel(" Value", fontsize= 14)
# plt.ylabel(" Square of Value",fontsize= 14)
# plt.tick_params(axis='both',labelsize= 14)
# plt.show()

# 绘制一个点
# import matplotlib.pyplot as plt

# plt.scatter(2, 4 , s = 200) # 实参s设置使用点的尺寸
# # 设置图标标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize = 24)
# plt.xlabel("Value", fontsize = 14)
# plt.ylabel("Square of value", fontsize = 14)

# # 设置刻度标记的大小
# plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# plt.show()

# # 绘制一系列点
# import matplotlib.pyplot as plt
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s = 100)

# #设置图标标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize = 24)
# plt.xlabel("Value", fontsize = 14)
# plt.ylabel("Square of value", fontsize = 14)

# # 设置刻度标记的大小
# plt.tick_params(axis = 'both', labelsize = 14)

# plt.show()

# 机器自动计算点的坐标生成图形
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, c = "red", edgecolor = 'none', s=40)  # c传递“颜色”参数

plt.title("Square Numbers", fontsize = 30)
plt.xlabel("Values", fontsize = 14)
plt.ylabel("Square of value", fontsize = 16)

plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches = 'tight') #保存图片，bbox是剪切掉多余的空白部分