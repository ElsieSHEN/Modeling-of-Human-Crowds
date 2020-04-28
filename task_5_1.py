import turtle
import numpy as np
import math
import draw_grid as dg
from utils import *

n = 100
#turtle.setup(800,1200)
task5_1 = Cellular(n, method='euclidean')

task5_1.set_grid(1)
task5_1.set_pedestrian(1, 50)
task5_1.set_target(101, 50)
for i in range(1,101):
    task5_1.set_obstacle(i, 40)
    task5_1.set_obstacle(i, 60)

for i in range(100):
    for p in task5_1.pedestrian:
        task5_1.next_step(p, n)
turtle.done()