import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click on points')

x = [4,7,9,11,5,6,7,4]
y = [1,2,3,4,5,6,7,6]

# line, = ax.plot(np.random.rand(100), 'o', picker=5)  # 5 points tolerance
line = ax.barh(x,y,picker=5)#, left=None)  # 5 points tolerance

def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xy()
    xdata = thisline.get_bbox()
    xdata = xdata.get_points()
    data = int(xdata[1][0])
    # xdata = thisline.get_xdata()
    # ydata = thisline.get_ydata()
    # ind = event.ind
    # print ('onpick points:', zip(xdata[ind], ydata[ind]))
    print("hello")
    print(xdata)
    print(data)
fig.canvas.mpl_connect('pick_event', onpick)

plt.show()