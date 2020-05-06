import turtle
from matplotlib import pyplot as plt
import numpy as np
import math
import draw_grid as dg
from utils import *

# 0: empty cell
# 1: pedestrian
# 2: obstacle
# 3: target

# remove: 1-remove cell after reach target / 0-don't remove

# dijk: 1-Dijkstra algorithm / 0-Distances matrix


n = 20
task0 = Cellular(n, method='euclidean', pedestrian=[], dijk=1)
#dg.init_grid(n)

task0.set_pedestrian(2,10,20)
task0.set_pedestrian(2,2,20)
               
task0.set_target(19,10)
task0.set_obstacle(10,5)
task0.set_obstacle(11,5)
task0.set_obstacle(12,5)
task0.set_obstacle(13,5)

task0.set_obstacle(13,6)
task0.set_obstacle(13,7)
task0.set_obstacle(13,8)
task0.set_obstacle(13,9)
task0.set_obstacle(13,10)
task0.set_obstacle(13,11)
task0.set_obstacle(13,12)
task0.set_obstacle(13,13)
task0.set_obstacle(13,14)
task0.set_obstacle(13,15)

task0.set_obstacle(12,15)
task0.set_obstacle(11,15)
task0.set_obstacle(10,15)
task0.set_obstacle(13,15)


#%matplotlib notebook

task0.set_board()
my_board = np.transpose(task0.grid)
fig = plt.gcf()
im = plt.imshow(my_board)

def animate(frame):
    im.set_data(task0.update_board(rmax=2))
    return im,

anim = animation.FuncAnimation(fig, animate, frames=200, 
                               interval=50)
plt.show()

#for i in range(50):
#    for p in task0.pedestrian:
#        task0.next_step(p, n, rmax=2)

#turtle.done()
#came_from, cost_so_far = task0.maybe_dijkstra(task0.target, task0.pedestrian)