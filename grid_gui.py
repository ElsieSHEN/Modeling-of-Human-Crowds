#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:07:04 2020

@author: ubuntujan
"""

from tkinter import *
import numpy as np

master = Tk();
n = 5                       #gridsize
mat = np.zeros((n,n))       #distance matrix
Width = 50                  #pixelwidth for GUI
(x, y) = (n,n)              #numner of cells for GUI
board = Canvas(master, width=x*Width, height =y*Width)
board.pack(side=LEFT)

for i in range(x):
        for j in range(y):
            board.create_rectangle(i*Width, j*Width, (i+1)*Width, (j+1)*Width, fill="white", width=1)
            
var = StringVar(master)
var.set("Select item")

option = OptionMenu(master, var, "pedestrian", "obstacle", "target")
option.pack()

def set_inital_conditions(event):
    x, y = int(event.x/50), int(event.y/50)
    print("x,y = ", x,y)
    if var.get() == "pedestrian":
        mat[x][y] = 1
        board.create_rectangle(x*Width, y*Width, (x+1)*Width, (y+1)*Width, fill = "green", width = 1)
    elif var.get() == "obstacle":
        mat[x][y] = 2
        board.create_rectangle(x*Width, y*Width, (x+1)*Width, (y+1)*Width, fill = "blue", width = 1)
    elif var.get() == "target":
        mat[x][y] = 10
        board.create_rectangle(x*Width, y*Width, (x+1)*Width, (y+1)*Width, fill = "red", width = 1)    
        
board.bind('<Button-1>', set_inital_conditions)
master.mainloop()

