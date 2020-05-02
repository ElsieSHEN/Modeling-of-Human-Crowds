import turtle
import numpy as np
import math
import draw_grid as dg

class Cellular():
    def __init__(self, n, method, pedestrian=[]):
        self.n = n       
        self.method = method
        self.pedestrian = pedestrian
        self.grid = np.zeros((self.n, self.n), dtype=int)
        self.dis_matrix = np.zeros(((self.n, self.n)))
    
    def set_grid(self, n):        
        dg.init_grid(self.n)

    def set_pedestrian(self, x, y):
        self.grid[x-1][y-1] = 1
        self.pedestrian.append(tuple((x, y)))
        dg.color_p(self.n, x, y)

    def set_target(self, x, y):
        self.grid[x-1][y-1] = 3
        dg.color_t(self.n, x, y)
        self.target = (x, y)

    def set_obstacle(self, x, y):
        self.grid[x-1][y-1] = 2
        dg.color_o(self.n, x, y)
        self.obstacle = (x, y)

    def set_dis_matrix(self, ped, rmax):
        a = self.target[0] - 1
        b = self.target[1] - 1
        
        for i in range(self.n):
            for j in range(self.n):
                dis = math.sqrt(((a-1)-i)**2 + ((b-1)-j)**2)/math.sqrt((self.n**2)*2)
                if self.grid[i][j] == 2:
                    dis += 999
                    
                if self.method == 'euclidean':
                    self.dis_matrix[i][j] = dis

                elif self.method == 'avoidance':                          
                    for k in self.pedestrian:
                        r = math.sqrt((i-k[0]+1)**2 + (j-k[1]+1)**2)                    
                        if r < rmax:
                            dis += math.exp(1/(r**2 - rmax**2))
                    self.dis_matrix[i][j] = dis
        # self.dis_matrix = self.dis_matrix / sum(self.dis_matrix)
        
        
    def find_next(self, ped, target, neighbors, rmax):
        self.set_dis_matrix(ped, rmax)
        tmp = [ped]
        tmp.extend(neighbors)
        distances = []

        for i in tmp:
            distances.append(self.dis_matrix[i[0]-1][i[1]-1])     

        idx = distances.index(min(distances))
        if idx == 0:
            return -1
        else:
            return idx-1

    def next_step(self, ped, n, rmax=0):
        idx_current = self.pedestrian.index(ped)
        neighbors = self.find_neighbors(ped[0], ped[1])
        for i in neighbors:
            if self.grid[i[0]-1][i[1]-1] == 3:
                return
        idx = self.find_next(ped, self.target, neighbors, rmax)

        if idx == -1:
            return
        next_cell = neighbors[idx]
        if self.grid[next_cell[0]-1][next_cell[1]-1] == 1:
            return
        self.pedestrian[idx_current] = next_cell
        self.grid[next_cell[0]-1][next_cell[1]-1] = 1
        dg.color_p(self.n, next_cell[0], next_cell[1])
        self.grid[ped[0]-1][ped[1]-1] = 0
        dg.color_e(self.n, ped[0], ped[1])
        self.get_there(next_cell)

    def find_neighbors(self, x, y):
        neighbors = []
        # p_neighbors = [(x+1, y), (x-1, y), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1), (x, y+1), (x, y-1)]
        p_neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for i in p_neighbors:
            a = i[0]
            b = i[1]
            if a > 0 and a <= self.n and b > 0 and b <= self.n:
                neighbors.append(i)
        return neighbors

    def get_there(self, next_cell):
        neighbors = self.find_neighbors(next_cell[0], next_cell[1])
        for i in neighbors:
            if self.grid[i[0]-1][i[1]-1] == 3:
                dg.color_e(self.n, next_cell[0], next_cell[1])
                self.grid[next_cell[0]-1][next_cell[1]-1] = 0
                self.pedestrian.remove(next_cell)
                return


    def not_dijkstra(self, tar, ped, step):
        self.set_dis_matrix(ped, rmax=0)
        neighbors = self.find_neighbors(tar[0], tar[1])
        cost = 0
        path = []
        visited = [tar]

        for s in range(step):
            cur_node = -1        
            cur_min = 9999
            for neighbor in neighbors:
                if self.grid[neighbor[0]-1][neighbor[1]-1] == 2:
                    visited.append(neighbor)
                if neighbor not in visited:
                    cur_dis = self.dis_matrix[neighbor[0]-1][neighbor[1]-1]
                    print(cur_dis)
                    visited.append(neighbor)
                    if cur_dis < cur_min:
                        cur_min = cur_dis
                        cur_node = neighbor
            if cur_node == -1: break                   
            path.append(cur_node)
            cost += cur_min     
                
            if cur_node == ped: break
            neighbors = self.find_neighbors(cur_node[0], cur_node[1])

        print(path)
        return path