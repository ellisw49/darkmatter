#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 16:37:26 2025

@author: mwilliams
"""

# applying the integrator with direct summation

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as ani


# call body.py
from Body import body 

# simuation parameters 

step = 50 # number of steps 
N = 1000    # number of bodies 
dt = 1     # time step 

# generate n bodies with initial positions and velocities
bodies = []
for n in range(N): 
    rx = np.random.uniform()
    ry = np.random.uniform()
    vx = np.random.uniform()  #normalized to 2*10^4
    vy = np.random.uniform()  #normalized to 2*10^4
    
    mass = np.random.uniform()
    color1 = "blue"
    
    b = body(rx, ry, vx, vy, mass, color1)
    bodies.append(b)


bodies = np.array(bodies)


# for each time step
for step in range(step):
    
    
    # creating position arrays for plotting
    rx_arr = []
    ry_arr = []

    # For each body in the system:
    for b in bodies:
        # reset force
        b.resetforce()

        # add force from all other bodies
        for other in bodies:
            if other is not b:
                b.addforce(other)
   
   # update position and velocity (advancing 1 time step)
    for b in bodies:
        b.update(dt)
        
        rx_arr.append(b.rx)
        ry_arr.append(b.ry)

    rx_arr = np.array(rx_arr)
    ry_arr = np.array(ry_arr)

    # show the plot of all bodies / add to movie 
    plt.scatter(rx_arr,ry_arr)
    plt.title(f"Timestep {step}")
    plt.show()
        
