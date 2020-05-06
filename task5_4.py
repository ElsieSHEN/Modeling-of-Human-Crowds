import turtle
import numpy as np
import math
import draw_grid as dg

from utils import *
from random import *

n = 125 #50m*50m plane 

task5_4 = Cellular(n, method='euclidean', pedestrian=[], target=[], remove=1, dijk=1)

task5_4.set_target(n, int(n/2))

empty_cell = []
for i in range(0, n):
    for j in range(0, n):
        if task5_4.grid[i][j] == 0:
            empty_cell.append((i+1, j+1))
            
random_p = sample(empty_cell, 50)

for i in range(7):
    for j in range(7):
        task5_4.set_pedestrian(random_p[j+i*7][0], random_p[j+i*7][1], age=20+i*10)
task5_4.set_pedestrian(random_p[49][0], random_p[49][1], age=20)        
        
#%matplotlib notebook

task5_4.set_board()

my_board = np.transpose(task5_4.grid)
fig = plt.gcf()
im = plt.imshow(my_board)


# Helper function that updates the board and returns a new image of
# the updated board animate is the function that FuncAnimation calls
def animate(frame):
    im.set_data(task5_4.update_board())        
    return im,

# This line creates the animation
anim = animation.FuncAnimation(fig, animate, frames=30, 
                               interval=250) #age 20 walking speed:1.6m/s, cell legth:0.4m
plt.show()


age=[20, 30, 40, 50, 60, 70, 80]
speed=np.zeros((7, 8))
n_speed = np.zeros(7)
avg_speed=[]

speed[0][0] = 1
for p in task5_4.stat:
    dist = p[1]*0.4
    time = p[2]*250/1000
    for i in range(7):
        if p[0] == 20+i*10:
            speed[i][int(n_speed[i])] = dist/time
            n_speed[i]+=1
            
for i in range(7):
    avg_speed.append(sum(speed[i])/n_speed[i])

#print(avg_speed)


plt.plot(age, avg_speed)
plt.ylim(0, 2.5)
plt.xlabel('age [years]')
plt.ylabel('horizontal walking speed [m/s]')
plt.show()