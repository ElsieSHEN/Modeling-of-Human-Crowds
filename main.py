import turtle
import numpy as np
import math
import re
import draw_grid as dg
from utils import *

rmax = 0
n = int(turtle.numinput("Grid", "Input the length of the grid", 50))

m = turtle.textinput("Cost function", "Choose the cost function (euclidean/avoidance): ")
if m == 'avoidance':
    rmax = turtle.numinput('rmax', 'Enter the value of rmax you want to set: ', 2)

Task = Cellular(n, method=m)

print('Initialize the grid now.')

Task.set_grid(n)

num_p = int(turtle.numinput("Pedestrian Number", "Enter the number of pedestrains you want to add: ", 1))
while num_p > 0:
    ped = turtle.textinput('Pedestrian', 'Enter the coordinate of your pedestrian (x, y): ')
    tmp = re.findall(r'[(](.*?)[)]', ped)[0].split(',')
    Task.set_pedestrian(int(tmp[0]), int(tmp[1]))
    num_p -= 1

num_t = int(turtle.numinput("Target Number", "Enter the number of targets you want to add: ", 1))
while num_t > 0:
    tar = turtle.textinput("Target", 'Enter the coordinate of your target: ')
    tmp = re.findall(r'[(](.*?)[)]', tar)[0].split(',')
    Task.set_target(int(tmp[0]), int(tmp[1]))
    num_t -= 1

num_o = int(turtle.numinput("Obstacle Number", "Enter the number of obstacles you want to add: ", 1))
while num_o > 0:
    obs = turtle.textinput('Obstacle', 'Enter the coordinate of your obstacle: ')
    tmp = re.findall(r'[(](.*?)[)]', obs)[0].split(',')
    Task.set_obstacle(int(tmp[0]), int(tmp[1]))
    num_o -= 1

step = int(turtle.numinput("Step", "Enter the number of steps you want to implement: ", 5))

for i in range(step):
    for p in Task.pedestrian:
        Task.next_step(p, n, rmax=rmax)
turtle.done()

print('Done')