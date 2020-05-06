import turtle
import numpy as np
import math
import draw_grid as dg
import time
from IPython import display
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

class Cellular():
    def __init__(self, n, method, pedestrian=[], target=[], remove=0, dijk=0, trans=0):
        self.n = n
        self.method = method
        self.pedestrian = pedestrian
        self.target = target
        self.grid = np.zeros((self.n, self.n), dtype=int)
        self.dis_matrix = np.zeros(((self.n, self.n)))
        self.dis_dijkstra = np.zeros((self.n, self.n))
        self.remove = remove     #flag:remove ped after reaching target
        self.dijk = dijk         #flag:calculate Dijkstra distance
        self.trans = trans        #flag:ignore transient response
        self.stat = []               #speed data for statistic
        self.total_iterations = 0       #passed time
        self.age_walk = np.array([[20,1],
                                 [30,0.969],
                                 [40,0.938],
                                 [50,0.906],
                                 [60,0.813],
                                 [70,0.688],
                                 [80,0.438]])
    
    #def set_grid(self, n):        
        #dg.init_grid(self.n)
        

    def set_pedestrian(self, x, y, age=20, count=0, iteration=0):
        self.grid[x-1][y-1] = 1
        self.pedestrian.append(tuple((x, y, age, count, iteration)))
        #dg.color_p(self.n, x, y)
    
    def set_target(self, x, y):#multiple target
        self.grid[x-1][y-1] = 3
        self.target.append(tuple((x, y)))
        #dg.color_t(self.n, x, y)

    def set_obstacle(self, x, y):
        self.grid[x-1][y-1] = 2
        #dg.color_o(self.n, x, y)
        self.obstacle = (x, y)                           
            
    
    def set_dis_matrix(self, rmax):
        for t in self.target:
            a = t[0] - 1
            b = t[1] - 1

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


                    
    def find_next_dijk(self, ped, neighbors, rmax):
        if self.method == 'avoidance':
            self.set_mtar_dijkstra_field()
            for i in range(self.n):
                for j in range(self.n):
                    for k in self.pedestrian:
                        r = math.sqrt((i-k[0]+1)**2 + (j-k[1]+1)**2)
                        if r < rmax:
                            dis = math.exp(1/(r**2 - rmax**2))
                            self.dis_dijkstra[i][j] += dis    
                                       
        tmp = [ped]
        tmp.extend(neighbors)
        distances = []
        
        for i in tmp:
            distances.append(self.dis_dijkstra[i[0]-1][i[1]-1])
            
        idx = distances.index(min(distances))
        if idx == 0:
            return -1
        else:
            return idx-1
    
    
    def find_next(self, ped, target, neighbors, rmax):
        if self.method == 'avoidance':
            self.set_dis_matrix(rmax)

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
                #dg.color_e(self.n, ped[0], ped[1])
                if self.remove == 1:
                    self.grid[ped[0]-1][ped[1]-1] = 0
                    self.stat.append((ped[2], ped[3], ped[4]))
                    self.pedestrian.remove(ped)
                    return -1
                return -1
        

        # initialize dijkstra field. If method is avoidance it will recalculate cost field([Yun]move it out)    
        #self.set_dijkstra_field(self.target)
        
        if self.dijk == 1:
            idx = self.find_next_dijk(ped, neighbors, rmax)
        else:
            idx = self.find_next(ped, self.target, neighbors, rmax)
           
        if idx == -1:
            return idx_current
        next_cell = neighbors[idx]           
        if self.grid[next_cell[0]-1][next_cell[1]-1] == 2:
            return idx_current
        if self.grid[next_cell[0]-1][next_cell[1]-1] == 1:
            return idx_current
        
       
        if self.trans == 1:
            if self.total_iterations>=30:
                #temporary tuple, so pedestrian (tuple) can continue to have their age (appending tuple)
                temp_tuple = next_cell + (ped[2], ped[3]+1, ped[4]) 
            else:
                temp_tuple = next_cell + (ped[2], ped[3], ped[4])
        else:
            temp_tuple = next_cell + (ped[2], ped[3]+1, ped[4])
        temp_tuple = next_cell + (ped[2], ped[3]+1, ped[4])
        self.pedestrian[idx_current] = temp_tuple
        self.grid[next_cell[0]-1][next_cell[1]-1] = 1
        #dg.color_p(self.n, next_cell[0], next_cell[1])
        self.grid[ped[0]-1][ped[1]-1] = 0
        #dg.color_e(self.n, ped[0], ped[1])

        return idx_current

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

    def get_there(self, next_cell):#not used
        neighbors = self.find_neighbors(next_cell[0], next_cell[1])
        for i in neighbors:
            if self.grid[i[0]-1][i[1]-1] == 3:
                dg.color_e(self.n, next_cell[0], next_cell[1])
                self.grid[next_cell[0]-1][next_cell[1]-1] = 0
                self.pedestrian.remove(next_cell)
                return
          
    def not_dijkstra(self, tar, ped, step):#not used
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
    
    def set_dijkstra_field(self):#not used
        tar = self.target
        frontier = [tar]
        came_from = {}
        came_from[tar] = None
        cost_so_far = {}
        cost_so_far[tar] = 0

        #dont include obstacles
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 2:
                    self.dis_dijkstra[i][j] = np.nan
        #dijkstra for grids            
        while frontier:
            curr = frontier.pop(0)         
            neighbors = self.find_neighbors(curr[0], curr[1])
            for neighbor in neighbors:
                new_cost = cost_so_far[curr] + 1
                if neighbor not in cost_so_far and (np.isnan(self.dis_dijkstra[neighbor[0]-1][neighbor[1]-1])==0):
                    cost_so_far[neighbor] = new_cost
                    self.dis_dijkstra[neighbor[0]-1][neighbor[1]-1] = new_cost
                    frontier.append(neighbor)
                    came_from[neighbor] = curr
        
        self.dis_dijkstra /= np.nanmax(self.dis_dijkstra)
        return came_from, cost_so_far, self.dis_dijkstra    
    
    def set_mtar_dijkstra_field(self):#multiple target
        self.dis_dijkstra = np.zeros((self.n, self.n))
        #dont include obstacles
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 2:
                    self.dis_dijkstra[i][j] = np.nan
               
        for tar in self.target:
            frontier = [tar]            
            came_from = {}
            came_from[tar] = None
            cost_so_far = {}
            cost_so_far[tar] = 0

            #dijkstra for grids            
            while frontier:
                curr = frontier.pop(0)         
                neighbors = self.find_neighbors(curr[0], curr[1])
                for neighbor in neighbors:
                    new_cost = cost_so_far[curr] + 1
                    if neighbor not in cost_so_far and (np.isnan(self.dis_dijkstra[neighbor[0]-1][neighbor[1]-1])==0):
                        a = self.dis_dijkstra[neighbor[0]-1][neighbor[1]-1]
                        if a == 0 or a > new_cost:
                            cost_so_far[neighbor] = new_cost
                            self.dis_dijkstra[neighbor[0]-1][neighbor[1]-1] = new_cost
                        else:
                            cost_so_far[neighbor] = a
                        frontier.append(neighbor)
                        came_from[neighbor] = curr
            
            came_from.clear()
            cost_so_far.clear()

        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 3:
                    self.dis_dijkstra[i][j] = 0
        
        self.dis_dijkstra /= np.nanmax(self.dis_dijkstra)
        return self.dis_dijkstra
    
    
    def set_board(self):
        if self.dijk == 1:
            self.set_mtar_dijkstra_field()
        else:
            self.set_dis_matrix(rmax=0)
            
    # returns the corresponding willingness to walk (given an certain age)       
    def get_prob_thresh(self, age):
        for i in range(self.age_walk.shape[0]):
            if age == self.age_walk[i][0]:
                res = self.age_walk[i][1]
        return res

    # determines if pedestrian moves in the current iteration
    def is_moving(self, ped):
        age = ped[2]
        #random number with 3 decimal places
        r = random.randint(0,1000) / 1000
        prob_threshold = self.get_prob_thresh(age)
        
        if r < prob_threshold:
            flag_move = 1
            return flag_move
        else:
            flag_move = 0
            return flag_move
            
    
    def update_board(self, rmax=0):
        for p in self.pedestrian:
            flag_move = self.is_moving(p)            
            idx_current = self.pedestrian.index(p)          
            if flag_move == 1:
                idx_current = self.next_step(p, self.n, rmax=rmax)
            if idx_current != -1:
                a = self.pedestrian[idx_current] 
                temp_tuple = (a[0], a[1], a[2], a[3], a[4]+1)
                if self.trans == 1:
                    if self.total_iterations >= 30:
                        self.pedestrian[idx_current] = temp_tuple
                else:
                    self.pedestrian[idx_current] = temp_tuple

        self.total_iterations += 1
        my_board = np.transpose(self.grid)
        return my_board
    

        

        