import turtle
import numpy as np
import math
import draw_grid as dg
from utils import *

# 0: empty cell
# 1: pedestrian
# 2: obstacle
# 3: target

task4 = Cellular(20, method='euclidean')

dg.init_grid(20)
task4.set_pedestrian(1, 10)
task4.set_target(20, 10)
task4.set_obstacle(17, 9)
task4.set_obstacle(18, 9)
task4.set_obstacle(18, 10)
task4.set_obstacle(18, 11)
task4.set_obstacle(17, 11)

# chicken test
for i in range(20):
    for p in task4.pedestrian:
        task4.next_step(task4.pedestrian[0], task4.n, rmax=0)
turtle.done()

# path = task4.not_dijkstra(task4.target, task4.pedestrian[0], 20)
# path.reverse()
# for cell in path:
#     ped = task4.pedestrian[0]
#     task4.pedestrian.remove(ped)
#     task4.set_pedestrian(cell[0], cell[1])
#     dg.color_e(task4.n, ped[0], ped[1])
# turtle.done()