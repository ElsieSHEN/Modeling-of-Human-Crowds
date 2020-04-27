import turtle
import numpy as np
import math
import draw_grid as dg
from utils import *

# 0: empty cell
# 1: pedestrian
# 2: obstacle
# 3: target

from utils import *

task3 = Cellular(50, 'cost')

dg.init_grid(50)
task3.set_pedestrian(10, 25)
task3.set_pedestrian(40, 25)
task3.set_pedestrian(25, 10)
task3.set_pedestrian(25, 40)
task3.set_pedestrian(40, 40) # for this pedestrian, step size is sqrt(2)

task3.set_target(25, 25)

for i in range(25):
    for p in task3.pedestrian:
        task3.next_step(p, 50)
turtle.done()