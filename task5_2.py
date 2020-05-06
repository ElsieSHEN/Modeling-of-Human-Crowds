import turtle
import numpy as np
import math
import draw_grid as dg

from utils import *
from random import *

# 0: empty cell
# 1: pedestrian
# 2: obstacle
# 3: target

# remove: 1-remove cell after reach target / 0-don't remove

# dijk: 1-Dijkstra algorithm / 0-Distances matrix


n = 140

task5_2 = Cellular(n, method='euclidean', pedestrian=[], target=[], remove=1, dijk=1, trans=1)



for i in range(64, 76):
    task5_2.set_target(140, i)
for i in range(1, 141):
    task5_2.set_obstacle(i, 63)
    task5_2.set_obstacle(i, 76)

# measuring points
for i in range(8, 13):
    for j in range(68, 73):
        task5_2.set_obstacle(i, j)

for i in range(133, 138):
    for j in range(65, 75):
        task5_2.set_obstacle(i, j)

empty_cell = []

for i in range(0, 140):
    for j in range(63, 75):
        if task5_2.grid[i][j] == 0:
            empty_cell.append((i+1, j+1))
    

n_ped = 134 #0.5P-134, 1P-269, 2P-538, 3P-806, 4P-1075, 5P-1344, 6P-1593
random_p = sample(empty_cell, n_ped)

for p in random_p:
    task5_2.set_pedestrian(p[0], p[1])


    
#for i in range(100):
#    for p in task5_2.pedestrian:
#        task5_2.next_step(p, n)
#turtle.done()


#%matplotlib notebook

task5_2.set_board()

my_board = np.transpose(task5_2.grid)
fig = plt.gcf()
im = plt.imshow(my_board)


# Helper function that updates the board and returns a new image of
# the updated board animate is the function that FuncAnimation calls
def animate(frame):
    im.set_data(task5_2.update_board())
    n_ped = 134 #0.5P-134, 1P-269, 2P-538, 3P-806, 4P-1075, 5P-1344, 6P-1593
    if len(task5_2.pedestrian) < n_ped:
        h = min(n_ped - len(task5_2.pedestrian), 12)
        width = [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
        y = sample(width, h)
        for j in y:
            if task5_2.grid[0][j-1]==0:
                task5_2.set_pedestrian(1, j)            
    return im,

# This line creates the animation
anim = animation.FuncAnimation(fig, animate, frames=30, 
                               interval=333)
plt.show()


for p in task5_2.pedestrian:
    task5_2.stat.append((p[2], p[3], p[4]))

speed=[]
for p in task5_2.stat:
    dist = p[1]*0.4
    time = p[2]*333/1000
    if time != 0:
        speed.append(dist/time)
print("total time: " ,round(task5_2.total_iterations/3, 3))
print("Average speed: " ,round(np.mean(speed), 3))