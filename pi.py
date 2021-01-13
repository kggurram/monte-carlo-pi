# import libraries
import numpy as np
import matplotlib.pyplot as plt 
import math

inc_c = 0 # points inside circle 
inc_s = 0 # points in square
n = 0

figure, axes = plt.subplots() # create graph foundation
draw_circle = plt.Circle((0.5, 0.5), 0.5, fill=False, zorder=10) # plot circle

axes.set_aspect(1) 
axes.add_artist(draw_circle) 

while(n<200): # only allow inputs above 200
    n = int(input("How many nodes would you like to input?\n[Please input a value of atleast 200]\n")) # ask user how many points to plot

cory = np.random.random_sample((n,)) # generate random x coordinate
corx = np.random.random_sample((n,)) # generate random y coordinate

for i in range(n): # for each point
    plt.plot(corx[i], cory[i], 'ro', alpha=0.1, zorder=5) # plot the point using coordinates

draw_circle = plt.Circle((0.5, 0.5), 0.5, fill=False) # draw the cirle

for i in range(n): # for each plot
    if((corx[i]*corx[i] + cory[i]*cory[i]) <= 1): # if selected random point is in circle
        inc_c += 1 # increment points plotted inside circle
        inc_s += 1 # increment total points plotted
    else:
        inc_s += 1 # increment total points only

pi = 4* (inc_c/inc_s) # estimate pi using ratio
print(pi) # print estimated pi

plt.title('Monte Carlo') # title of graph
plt.show() # show the graph