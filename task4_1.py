import turtle
import numpy as np
import math
import draw_grid as dg
from utils import *

# 0: empty cell
# 1: pedestrian
# 2: obstacle
# 3: target

n = 88
task4_1 = Cellular(n, method='avoidance')

dg.init_grid(n)


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
         

# set pedestrians
for i in range(1,17,2):
    for j in range(27,62,2):
        task4_1.set_pedestrian(i,j)
               

task4_1.set_target(88, 44)


for i in range(200):
    for p in task4_1.pedestrian:
        task4_1.next_step(p, n, rmax=2)
    
turtle.done()