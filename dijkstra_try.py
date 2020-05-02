#import turtle
from matplotlib import pyplot as plt
import numpy as np
import math
#import draw_grid as dg
from utils import *

# 0: empty cell
# 1: pedestrian
# 2: obstacle
# 3: target

n = 5
task0 = Cellular(n, method='euclidean')

#ListofImages.append(task4_1.grid)


#dg.init_grid(n)

"""
# set horizontal walls
for i in range(1,88):
    j1 = 26
    j2 = 62
    if (i > 35 and i < 53):
        j1 += 15    
        j2 -= 15
    task4_1.set_obstacle(i,j1)
    task4_1.set_obstacle(i,j2)
    
# set vertical walls
i_v = [35,53,88]    
for j in range(26,62):
    for i in i_v:
        if (j > 41 and j < 47 ):
            continue
        
        task4_1.set_obstacle(i,j)
         
"""
# set pedestrians

task0.set_pedestrian(1,1)
               
task0.set_target(4,4)
task0.set_obstacle(3,2)

for i in range(5):
    for p in task0.pedestrian:
        task0.next_step(p, n, rmax=4)


#came_from, cost_so_far = task0.maybe_dijkstra(task0.target, task0.pedestrian)