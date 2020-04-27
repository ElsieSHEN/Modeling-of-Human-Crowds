#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:07:04 2020

@author: ubuntujan
"""

from tkinter import *
import numpy as np
import math
from dataclasses import dataclass
from collections import namedtuple
from matplotlib import pyplot as plt
import matplotlib.animation as animation

   
PedestrianList = []    
master = Tk();
n = 5                                       #inner gridsize (+2 for boundary)
max_dist = math.sqrt((n-1)**2 + (n-1)**2)
mat_state = np.ones((n+2,n+2)) 
mat_obst = np.ones((n+2,n+2))            #needed for padding, boundary is initialized with ones
inner_matrix = np.zeros((n,n)) 
mat_state[1:inner_matrix.shape[0]+1, 1:inner_matrix.shape[1]+1]=inner_matrix#distance matrix
mat_obst[1:inner_matrix.shape[0]+1, 1:inner_matrix.shape[1]+1]=inner_matrix#distance matrix
mat_dist = np.zeros((n+2,n+2))
Width = 50                       #pixelwidth for GUI
(x, y) = (n+2,n+2)              #numner of cells for GUI
t_coord = [int] * 2               #initialize target coordiantes as mutable object
#Pedestrian = namedtuple("Pedestrian", "py px mat_cost")


@dataclass
class Pedestrian:
    py: int
    px: int
    mat_cost: np.ndarray

    
board = Canvas(master, width=x*Width, height =y*Width)
board.pack(side=LEFT)

for i in range(x):
        for j in range(y):
            if (i==0 or i==n+1 or j==0 or j==n+1):
                board.create_rectangle(i*Width, j*Width, (i+1)*Width, (j+1)*Width, fill="blue", width=1)
            else:   
                board.create_rectangle(i*Width, j*Width, (i+1)*Width, (j+1)*Width, fill="white", width=1)
            
var = StringVar(master)
var.set("Select item")

option = OptionMenu(master, var, "pedestrian", "obstacle", "target")
""" Encoding grid states:
    0: Empty
    1: Obstacle
    2: Pedestrian
    3: Target
"""    
option.pack()

def set_inital_conditions(event):
    x, y = int(event.x/50), int(event.y/50)
    print("x,y = ", x,y)
    print(type(x))
    if var.get() == "pedestrian":
        mat_state[y][x] = "2" 
        PedestrianList.append(Pedestrian(y,x, np.zeros((n+2,n+2))))
        board.create_rectangle(x*Width, y*Width, (x+1)*Width, (y+1)*Width, fill = "green", width = 1)
    elif var.get() == "obstacle":
        mat_state[y][x] = "1"
        mat_obst[y][x] = 1
        board.create_rectangle(x*Width, y*Width, (x+1)*Width, (y+1)*Width, fill = "blue", width = 1)
    elif var.get() == "target":
        mat_state[y][x] = "3"
        t_coord[0] = x
        t_coord[1] = y
        board.create_rectangle(x*Width, y*Width, (x+1)*Width, (y+1)*Width, fill = "yellow", width = 1)       
             
board.bind('<Button-1>', set_inital_conditions)
master.mainloop()

"""
Takes in coordinates and the size of the complete grid (with boundaries) and 
calculates the distance for each grid cell in the inner grid
"""
def distance_field(target_coord, n, mat_dist, max_dist):
    for x in range(1,n+1):
        for y in range(1,n+1):
            mat_dist[y][x] = (math.sqrt((target_coord[0]-x)**2 + (target_coord[1]-y)**2))/max_dist                 
    
distance_field(t_coord, n, mat_dist, max_dist)
   
#initialize cost_field (for each pedestrian later) with immutable fields (distance field, obstacle field)
for P in PedestrianList:
    P.mat_cost = mat_dist + mat_obst 
     
ListIterationVisualization = [mat_state]
def loop_neighbours(Ped):
    temp_u = 1
    py = Ped.py
    px = Ped.px
    #new_y, new_x = Ped.py, Ped.px    
    for y in range(py-1, py+2):
        for x in range(px-1, px+2):
            temp_u_new = Ped.mat_cost[y][x]
            if temp_u_new == 0:
                return temp_u_new
            elif temp_u_new < temp_u:
                new_x = x
                new_y = y
                temp_u = temp_u_new
    mat_state[new_y][new_x] = 2
    mat_state[py][px] = 0
    Ped.py = new_y
    Ped.px = new_x
    plt.imshow(mat_state)
    plt.show()
   
eps = 1
    
while (eps != 0):                                       
    eps = loop_neighbours(PedestrianList[0])
    ListIterationVisualization.append(mat_state)
"""
for img in range(len(ListIterationVisualization)):
    plt.imshow(ListIterationVisualization[img])
    plt.pause(2)
    plt.show()
    
"""    

    
"""
def showvisualizationslider(step):
    plt.figure()
    plt.imshow(ListIterationVisualization[step])
       
interact(showvisualizationslider, step=widgets.IntSlider(min=0, max=4, step=1, values=0))    
    
def utility_function(t_x, t_y, x,y, state):
    u = 0
    if x==y:                #the grid cell itself
        u = 0.8
        return u
    elif state == 3:
        return
    elif state == 2:
        u = 0.9
        return u
    elif state == 1:
        u = 1.1
        return u
    elif state == 0:
        u = (math.sqrt((t_x-x)**2 + (t_y-y)**2)) / max_dist
"""