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

n = 20
task0 = Cellular(n, method='avoidance')
dg.init_grid(n)

task0.set_pedestrian(2,10)
task0.set_pedestrian(2,2)
               
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


for i in range(50):
    for p in task0.pedestrian:
            task0.next_step(p, n, rmax=2)

turtle.done()
#came_from, cost_so_far = task0.maybe_dijkstra(task0.target, task0.pedestrian)