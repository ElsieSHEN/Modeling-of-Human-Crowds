import turtle
import numpy as np
import math
import draw_grid as dg
from utils import *

# 0: empty cell
# 1: pedestrian
# 2: obstacle
# 3: target

# remove: 1-remove cell after reach target / 0-don't remove

# dijk: 1-Dijkstra algorithm / 0-Distances matrix


task2 = Cellular(50, method='euclidean', pedestrian=[])

#dg.init_grid(50)
task2.set_pedestrian(5, 25)
task2.set_target(25, 25)

#for i in range(25):
#    task2.next_step(task2.pedestrian[0], 50)
#turtle.done()


##### Animate the board #####
# This will throw an error the first time you run the code, but the program will run properly if you
# execute the cell again (there is an error with the animation package that I cannot seem to get rid of)

# Required line for plotting the animation
%matplotlib notebook

#draw distance matrix
task2.set_board()

# Initialize the board
my_board = np.transpose(task2.grid)

# Initialize the plot of the board that will be used for animation
fig = plt.gcf()

# Show first image - which is the initial board
im = plt.imshow(my_board)
plt.show()

# Helper function that updates the board and returns a new image of
# the updated board animate is the function that FuncAnimation calls
def animate(frame): #frame is an int from 0 to frames-1, and keep looping
    im.set_data(task2.update_board())
    return im,

# This line creates the animation
anim = animation.FuncAnimation(fig, animate, frames=25, 
                               interval=100)