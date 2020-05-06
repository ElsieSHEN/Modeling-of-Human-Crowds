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

task4 = Cellular(20, method='avoidance', pedestrian=[], dijk=1)

#dg.init_grid(20)
task4.set_pedestrian(1, 10)
task4.set_target(20, 10)
task4.set_obstacle(17, 9)
task4.set_obstacle(18, 9)
task4.set_obstacle(18, 10)
task4.set_obstacle(18, 11)
task4.set_obstacle(17, 11)

#%matplotlib notebook

task4.set_board()
my_board = np.transpose(task4.grid)

fig = plt.gcf()

im = plt.imshow(my_board)


def animate(frame):
    im.set_data(task4.update_board(rmax=2))
    return im,

anim = animation.FuncAnimation(fig, animate, frames=200, 
                               interval=100)
plt.show()