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



n = 100

#turtle.setup(800,1200)
task5_1 = Cellular(n, method='euclidean', pedestrian=[], dijk=1)

#task5_1.set_grid(1)
task5_1.set_pedestrian(1, 50, age = 20)
task5_1.set_target(100, 50)

for i in range(1,101):
    task5_1.set_obstacle(i, 47)
    task5_1.set_obstacle(i, 53)

   
#for i in range(100):
#    for p in task5_1.pedestrian:
#        task5_1.next_step(p, n)
#turtle.done()
        

#%matplotlib notebook


task5_1.set_board()

my_board = np.transpose(task5_1.grid)
fig = plt.gcf()
im = plt.imshow(my_board)


def animate(frame):
    im.set_data(task5_1.update_board())
    return im,

anim = animation.FuncAnimation(fig, animate, frames=500, 
                               interval=333)
plt.show()

print("total time: " ,round(task5_1.total_iterations/3, 3))