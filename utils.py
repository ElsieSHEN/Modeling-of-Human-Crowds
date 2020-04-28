import turtle
import numpy as np
import math
import draw_grid as dg

class Cellular():
    def __init__(self, n, method, pedestrian=[]):
        self.n = n
        self.grid = np.zeros((self.n, self.n), dtype=int)
        self.method = method
        self.pedestrian = pedestrian
    
    def set_pedestrian(self, x, y):
        self.grid[x-1][y-1] = 1
        self.pedestrian.append(tuple((x, y)))
        dg.color_p(50, x, y)

    def set_target(self, x, y):
        self.grid[x-1][y-1] = 3
        dg.color_t(50, x, y)
        self.target = (x, y)


    def find_next(self, ped, target, neighbors, method, rmax):
        distances = []
        x = target[0]
        y = target[1]
        if self.method == 'euclidean':             
            for i in neighbors: 
                a = i[0]
                b = i[1]
                dis = math.sqrt((x-a)**2 + (y-b)**2)               
                distances.append(dis)
            idx = distances.index(min(distances)) 
            return idx     
        elif self.method == 'avoidance':
            tmp = [ped]
            tmp.extend(neighbors)
            for i in tmp:
                a = i[0]
                b = i[1]
                dis = math.sqrt((x-a)**2 + (y-b)**2)
                for j in self.pedestrian:
                    r = math.sqrt((a-j[0])**2 + (b-j[1])**2)
                    if r < rmax:
                        dis = math.exp(1/(r**2 - rmax**2)) + dis
                distances.append(dis)

            min_dis = min(distances)
            idx = distances.index(min_dis)
            
            if idx == 0:
                idx = -1
                
            return idx

    def next_step(self, ped, n, method='euclidean', rmax=0):
        idx_current = self.pedestrian.index(ped)
        neighbors = find_neighbors(ped[0], ped[1], n)
        for i in neighbors:
            if self.grid[i[0]-1][i[1]-1] == 3:
                return
        idx = self.find_next(ped, self.target, neighbors, method, rmax)
        if idx == -1:
            return
        next_cell = neighbors[idx-1]
        self.pedestrian[idx_current] = next_cell
        self.grid[next_cell[0]-1][next_cell[1]-1] = 1
        dg.color_p(50, next_cell[0], next_cell[1])
        self.grid[ped[0]-1][ped[1]-1] = 0
        dg.color_e(50, ped[0], ped[1])


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