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

task2 = Cellular(50, method='euclidean')

dg.init_grid(50)
task2.set_pedestrian(5, 25)
task2.set_target(25, 25)
for i in range(25):
    task2.next_step(task2.pedestrian[0], 50)
turtle.done()