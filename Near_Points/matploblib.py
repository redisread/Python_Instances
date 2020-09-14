import matplotlib.pyplot as plt

fig = plt.figure()  # 创建画板
ax = fig.add_subplot(111)   # 轴线建立
ax.set(xlim=[0, 1000], ylim=[0, 1000], title='A Planar Coordinate System',
       ylabel='Y-Axis', xlabel='X-Axis')

a = [[200, 300], [300, 500]]
b = [[400, 600], [350, 430]]
plt.plot([200, 300, 500], [100, 200, 100], color='r')     # ([200,300],[400,600])
plt.scatter([200, 300, 500], [100, 200, 100], color='b')
plt.show()
