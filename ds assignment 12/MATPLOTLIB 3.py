from matplotlib import pyplot as plt
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
label="BMW",width=.5)
plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
label="Audi", color='r',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()

x = [1,1.5,2,2.5,3,3.5,3.6]
y = [7.5,8,8.5,9,9.5,10,10.5]
x1=[8,8.5,9,9.5,10,10.5,11]
y1=[3,3.5,3.7,4,4.5,5,5.2]
plt.scatter(x,y, label='high income low saving',color='r')
plt.scatter(x1,y1,label='low income high savings',color='b')
plt.xlabel('saving*100')
plt.ylabel('income*1000')
plt.title('Scatter Plot')
plt.legend()
plt.show()

days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]
plt.plot([], [], color='m', label='Sleeping', linewidth=5)
plt.plot([], [], color='c', label='Eating', linewidth=5)
plt.plot([], [], color='r', label='Working', linewidth=5)
plt.plot([], [], color='k', label='Playing', linewidth=5)
plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot')
plt.legend()
plt.show()

days = [1,2,3,4,5]
sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working =[7,8,7,2,2]
playing = [8,5,7,8,13]
slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']
plt.pie(slices,
  labels=activities,
  colors=cols,
  startangle=90,
  shadow= True,
  explode=(0,0.1,0,0),
  autopct='%1.1f%%')
plt.title('Pie Plot')
plt.show()

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [50,40,70,80,20]
y2 = [80,20,20,50,60]
y3 = [70,20,60,40,60]
y4 = [80,20,20,50,60]
plt.plot(x,y,'g',label='Enfield', linewidth=5)
plt.plot(x,y2,'c',label='Honda',linewidth=5)
plt.plot(x,y3,'k',label='Yahama',linewidth=5)
plt.plot(x,y4,'y',label='KTM',linewidth=5)
plt.title('bike details in line plot')
plt.ylabel('Distance in km')
plt.xlabel('Days')
plt.legend()

plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="Enfield", width=0.5)
plt.bar([0.26,1.25,2.25,3.25,4.25],[80,20,20,50,60],label="Honda", color='r', width=0.5)
plt.bar([0.31,1.5,2.5,3.5,4.5],[70,20,60,40,60], label="Yamaha", color='y', width=0.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="KTM", color='g', width=0.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Bikes details in BAR PLOTTING')
plt.show()

days = [1, 2, 3, 4, 5]
Enfield = [50, 40, 70, 80, 20]
Honda = [80, 20, 20, 50, 60]
Yahama = [70, 20, 60, 40, 60]
KTM = [80, 20, 20, 50, 60]
plt.plot([], [], color='k', label='Enfield', linewidth=5)
plt.plot([], [], color='c', label='Honda', linewidth=5)
plt.plot([], [], color='y', label='Yahama', linewidth=5)
plt.plot([], [], color='m', label='KTM', linewidth=5)
plt.stackplot(days, Enfield, Honda, Yahama, KTM, colors=['k', 'c', 'y', 'm'])
plt.xlabel('Days')
plt.ylabel('Distance in kms')
plt.title('Bikes details in area plot')
plt.legend()
plt.show()

days = [1, 2, 3, 4, 5]
Y1 = [50, 40, 70, 80, 20]
Y2 = [80, 20, 20, 50, 60]
Y3 = [70, 20, 60, 40, 60]
Y4 = [80, 20, 20, 50, 60]
plt.scatter(days, Y1, label='Enfield', color='r')
plt.scatter(days, Y2, label='Honda', color='b')
plt.scatter(days, Y3, label='Yahama', color='y')
plt.scatter(days, Y4, label='KTM', color='k')
plt.xlabel('Days')
plt.ylabel('Distance in kms')
plt.title('Bike details in Scatter Plot')
plt.legend()
plt.show()

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [1, 2, 3, 4, 5]
y = [50, 40, 70, 80, 20]
y2 = [80, 20, 20, 50, 60]
y3 = [70, 20, 60, 40, 60]
y4 = [80, 20, 20, 50, 60]
ax.plot(x, y, 'g', label='Enfield', linewidth=5)
ax.plot(x, y2, 'c', label='Honda', linewidth=5)
ax.plot(x, y3, 'k', label='Yahama', linewidth=5)
ax.plot(x, y4, 'y', label='KTM', linewidth=5)
ax.set_title('Bike details in line plot')
ax.set_xlabel('Days')
ax.set_ylabel('Distance in kms')
ax.set_zlabel('Z-axis (optional)')
ax.legend()
plt.show()