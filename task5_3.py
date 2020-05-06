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


test3 = Cellular(50, method='avoidance', pedestrian=[], remove=1, dijk=1)

#dg.init_grid(50)
for i in range(34, 18, -2):
    test3.set_pedestrian(i, 46)
    test3.set_pedestrian(i, 50)
    if i >= 22 and i % 4 == 2:
        test3.set_pedestrian(i-1, 48)

    test3.set_obstacle(i, 45)
    test3.set_obstacle(i-1, 45)
    test3.set_obstacle(45, i)
    test3.set_obstacle(45, i-1)

for i in range(10):
    test3.set_obstacle(35+i, 45)
    test3.set_obstacle(45, 35+i)
    test3.set_obstacle(18-i, 45)
    test3.set_obstacle(45, 18-i)

test3.set_obstacle(45, 45)

test3.set_target(50, 1)

#for i in range(100):
#    for p in test3.pedestrian:
#        test3.next_step(p, 50, rmax=1)
#turtle.done()

# %matplotlib notebook

test3.set_board()

my_board = np.transpose(test3.grid)
fig = plt.gcf()
im = plt.imshow(my_board)


# Helper function that updates the board and returns a new image of
# the updated board animate is the function that FuncAnimation calls
def animate(frame):
    im.set_data(test3.update_board(rmax=1.5))
    return im,

# # This line creates the animation
anim = animation.FuncAnimation(fig, animate, frames=200, 
                               interval=50)

plt.show()