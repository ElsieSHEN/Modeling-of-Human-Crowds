import turtle
import numpy as np
import math
import draw_grid as dg
from utils import *

test3 = Cellular(50, method='avoidance')

dg.init_grid(50)
for i in range(48, 38, -1):
    test3.set_pedestrian(i, 49)
    test3.set_pedestrian(i, 50)
    test3.set_obstacle(i, 48)
    test3.set_obstacle(48, i)
test3.set_target(50, 1)
for i in range(100):
    for p in test3.pedestrian:
        test3.next_step(p, 50, rmax=1)
turtle.done()