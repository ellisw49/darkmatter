#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 16:32:24 2025

@author: mwilliams
"""  

# applying the integrator with the barnes-hut tree method

# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
 
# importing classes from other files

from Body import body
from Quad import quad
from Tree import tree
import Initialize as init
from nbody_anim import animate_simulation


# generate N bodies with initial positions and velocities


N = 500 # number of bodies
dt = 0.1
step = 300 # number of steps

# defining particle properties

#mass = 10e31 # uniform mass in kg
#color1 = "red"
windowsize = 10 # AU
#vrange = 2e4 # maximum velocity


bodies = init.makebodies_test(N)

# def make_body():
#     #rx = windowsize * np.random.uniform()
#     #ry = windowsize * np.random.uniform()
#     rx = np.random.normal()
#     ry = np.random.normal()
#     vx = np.random.normal()
#     vy = np.random.normal()
    
#     b = body(rx,ry,vx,vy,mass,color1)
#     return b

# # making all of the N bodies
# bodies = []

# for i in range(N):
#     bodies.append(make_body())

#bodies = np.array(bodies)

# initialize code to make movie

# create new bhtree for all bodies on the screen
og_quad = quad(windowsize/2,windowsize/2,windowsize)
this_tree = tree(og_quad)

# lists to store all positions FOR ANIMATION
all_rx_arrs = []
all_ry_arrs = []


def barnes_hut_step(bodies, dt):
    # build tree each step
    og_quad = quad(windowsize/2, windowsize/2, windowsize)
    this_tree = tree(og_quad)

    
    for b in bodies:
        this_tree.insert(b)

    # compute forces
    for b in bodies:
        b.resetforce()
        this_tree.update_force(b)

    # update positions
    for b in bodies:
        b.update(dt, 4, "BH", bodies)

# run animation
animate_simulation(
    bodies=bodies,
    step_function=barnes_hut_step,
    frames=step,
    dt=dt,
    save="bh.gif"
)
plt.show()



# # stepping through time
# for step in range(step):
    
#     # creating new tree and subdividing the tree as needed with insert method
#     this_tree = tree(og_quad)
#     for b in bodies:
#         this_tree.insert(b)
    
#     # creating position arrays for plotting - for regular plotting
#     rx_arr = []
#     ry_arr = []
    
#     # for all bodies in the tree:
#     for b in bodies:
        
#         # reset force to zero
#         b.resetforce()
        
            
#         # calculating new force
#         this_tree.update_force(b)
        
    
        
#     # second for loop to update positions and make plot at each step
#     for b in bodies:
        
#         #update positions by 1 time step
#         #b.update(dt, 4 , 'BH')
#         b.update(dt, 4, 'BH', this_tree)
                
#         rx_arr.append(b.rx)
#         ry_arr.append(b.ry)

#     # show the plot of all bodies / add to movie 
#     plt.scatter(rx_arr,ry_arr)
#     # plt.xlim(-windowsize, windowsize)
#     # plt.ylim(-windowsize, windowsize)
#     plt.title(f"Timestep {step}")
#     plt.show()
