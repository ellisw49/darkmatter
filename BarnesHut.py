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

# generate N bodies with initial positions and velocities

N = 100 # number of bodies
dt = 1 # time step in seconds
step = 100 # number of steps

# defining particle properties

mass = 10e41 # uniform mass in kg
color1 = "red"
windowsize = 3.086e22 # 1 Mpc
vrange = 2e4 # maximum velocity

def make_body():
    rx = windowsize * np.random.uniform()
    ry = windowsize * np.random.uniform()
    vx = vrange * np.random.uniform()
    vy = vrange * np.random.uniform()
    
    b = body(rx,ry,vx,vy,mass,color1)
    return b

# making all of the N bodies
bodies = []

for i in range(N):
    bodies.append(make_body())

bodies = np.array(bodies)

# initialize code to make movie

# create new bhtree for all bodies on the screen
og_quad = quad(0,0,windowsize)
this_tree = tree(og_quad)


# stepping through time
for step in range(step):
    
    # creating new tree and subdividing the tree as needed with insert method
    this_tree = tree(og_quad)
    for b in bodies:
        this_tree.insert(b)
    
    # creating position arrays for plotting
    rx_arr = []
    ry_arr = []
    
    # for all bodies in the tree:
    for b in bodies:
        
        # reset force to zero
        b.resetforce()
            
                
        # if body in q:
        if this_tree.quad.contains(b.rx,b.ry):
            
            # calculating new force
            this_tree.update_force(b)
        
    # second for loop to update positions and make plot at each step
    for b in bodies:
        
        #update positions by 1 time step
        b.update(dt)
                
        rx_arr.append(b.rx)
        ry_arr.append(b.ry)

    # update plot / movie / graphic for all bodies
    rx_arr = np.array(rx_arr)
    ry_arr = np.array(ry_arr)

    # show the plot of all bodies / add to movie 
    plt.scatter(rx_arr,ry_arr)
    plt.title(f"Timestep {step}")
    plt.show()
        
