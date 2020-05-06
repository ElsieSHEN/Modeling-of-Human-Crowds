import turtle
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


task3 = Cellular(50, method='avoidance', pedestrian=[])

#dg.init_grid(50)
task3.set_pedestrian(10, 25)
task3.set_pedestrian(25, 10)
task3.set_pedestrian(40, 25)
task3.set_pedestrian(40, 40) # for this pedestrian, step size is sqrt(2)
task3.set_pedestrian(25, 40)

task3.set_target(25, 25)

#for i in range(10):
#    for p in task3.pedestrian:
#        task3.next_step(p, 50, rmax=4)
#turtle.done()

#%matplotlib notebook
task3.set_board()
my_board = np.transpose(task3.grid)
fig = plt.gcf()
im = plt.imshow(my_board)


def animate(frame):
    im.set_data(task3.update_board(rmax=4))
    return im,

anim = animation.FuncAnimation(fig, animate, frames=200, 
                               interval=50)
plt.show()