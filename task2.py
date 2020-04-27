import turtle
import numpy as np
import math
import draw_grid as dg

# 0: empty cell
# 1: pedestrian
# 2: obstacle
# 3: target

global grid
global pedestrian

pedestrian = []
target = tuple()

def find_neighbors(x, y, n):
    neighbors = []
    p_neighbors = [(x+1, y), (x-1, y), (x+1, y+1), (x+1, y-1), 
                   (x-1, y+1), (x-1, y-1), (x, y+1), (x, y-1)]
    for i in p_neighbors:
        a = i[0]
        b = i[1]
        if a >= 0 and a < n and b >= 0 and b < n:
            neighbors.append(i)
    return neighbors
  
def set_pedestrian(x, y):
    grid[x][y] = 1
    pedestrian.append(tuple((x, y)))
    dg.color_p(50, x, y)

def set_target(x, y):
    grid[x][y] = 3
    dg.color_t(50, x, y)
    target = (x, y)

def cost(ped, neighbors, method='euclidean', rmax=0):
    distances = []
    x = ped[0]
    y = ped[1]
    for i in neighbors:
        a = i[0]
        b = i[1]
        dis = math.sqrt((x-a)**2 + (y-b)**2)
        if method == 'euclidean':             
            distances.append(dis)
        elif method == 'avoidance':
            if dis >= rmax:
                distances.append(0)
            else:
                val = math.exp(1/(dis**2 - rmax**2))
                distances.append(val)
    print(distances)
    return distances

def next_step(ped, n, method='euclidean', rmax=0):
    neighbors = find_neighbors(ped[0], ped[1], n)
    for i in neighbors:
        if grid[i[0]][i[1]] == 3:
            return
    distances = cost(ped, neighbors, method, rmax)
    idx = distances.index(min(distances))
    next_cell = neighbors[idx]
    pedestrian.append(next_cell)
    grid[next_cell[0]][next_cell[1]] = 1
    dg.color_p(50, next_cell[0], next_cell[1])
    pedestrian.remove(ped)
    grid[ped[0]][ped[1]] = 0
    dg.color_e(50, ped[0], ped[1])


def task2():
    grid = np.zeros((50, 50), dtype=int)
    dg.init_grid(50)
    set_pedestrian(5, 25)
    set_target(25, 25)
    for i in range(25):
        next_step(pedestrian[0], 50)
    turtle.done()

task2()