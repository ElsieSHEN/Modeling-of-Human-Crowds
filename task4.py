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

# chicken test
#for i in range(20):
#    for p in task4.pedestrian:
#        task4.next_step(task4.pedestrian[0], task4.n, rmax=2)
#turtle.done()



# path = task4.not_dijkstra(task4.target, task4.pedestrian[0], 20)
# path.reverse()
# for cell in path:
#     ped = task4.pedestrian[0]
#     task4.pedestrian.remove(ped)
#     task4.set_pedestrian(cell[0], cell[1])
#     dg.color_e(task4.n, ped[0], ped[1])
# turtle.done()

%matplotlib notebook

task4.set_board()
my_board = np.transpose(task4.grid)

fig = plt.gcf()

im = plt.imshow(my_board)
plt.show()

def animate(frame):
    im.set_data(task4.update_board(rmax=2))
    return im,

anim = animation.FuncAnimation(fig, animate, frames=200, 
                               interval=100)