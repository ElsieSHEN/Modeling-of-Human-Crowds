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


n = 70

task5_2 = Cellular(n, method='euclidean', pedestrian=[])

#dg.init_grid(n)

for i in range(1, 71):
    for j in range(31, 41):
        if i % 2 != 0:
            if j % 2 != 0:
                if (i, j) != (11, 35) and (i, j) != (61, 35) and (i, j) != (61, 37):
                    task5_2.set_pedestrian(i, j)
        else:
            if j % 2 == 0:
                if (i, j) != (10, 36) and (i, j) != (60, 34) and (i, j) != (60, 36):
                    task5_2.set_pedestrian(i, j)

#for i in range(31, 41):
#    task5_2.set_target(70, i)
task5_2.set_target(70, 35)
for i in range(1, 71):
    task5_2.set_obstacle(i, 30)
    task5_2.set_obstacle(i, 41)

# control measuring points
task5_2.set_obstacle(10, 35)
task5_2.set_obstacle(11, 35)
task5_2.set_obstacle(10, 36)
task5_2.set_obstacle(11, 36)

# main measuring points
task5_2.set_obstacle(60, 34)
task5_2.set_obstacle(61, 34)
task5_2.set_obstacle(60, 35)
task5_2.set_obstacle(61, 35)

# control measuring points
task5_2.set_obstacle(60, 36)
task5_2.set_obstacle(61, 36)
task5_2.set_obstacle(60, 37)
task5_2.set_obstacle(61, 37)

    
#for i in range(100):
#    for p in task5_2.pedestrian:
#        task5_2.next_step(p, n)
#turtle.done()


%matplotlib notebook

task5_2.set_board()

my_board = np.transpose(task5_2.grid)
fig = plt.gcf()
im = plt.imshow(my_board)


def animate(frame):
    im.set_data(task5_2.update_board())
    #for i in range(31, 41, 2):
    #    task5_2.set_pedestrian(1, i)
    return im,


anim = animation.FuncAnimation(fig, animate, frames=30, 
                               interval=100)
plt.show()