#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 16:37:26 2025

@author: mwilliams
"""

# applying the integrator with direct summation



# call body.py

# generate n bodies with initial positions and velocities

# for each time step

    # for each body
    
        # reset the force on this body
    
        # add the force between this body and all other bodies
        
        # update position and velocity (advancing 1 time step)
        
        
        
        # plot the body's new position
        
    
    # show the plot of all bodies / add to movie
    
    # advance to next time step
    

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as ani


from Body import body 

# simuation parameters 

step = 100 # number of steps 
N = 200    # number of bodies 
dt = 1     # time step 

bodies = []
for n in range(N): 
    rx = np.random.uniform()
    ry = np.random.uniform()
    vx = np.random.uniform()  #normalized to 2*10^4
    vy = np.random.uniform()  #normalized to 2*10^4
    
    mass = np.random.uniform()
    
    
# ----------------------------
# 3. Main time integration loop
# ----------------------------
for step in range(step):

    # For each body in the system:
    for b in bodies:
        # reset force
        b.reset_force()

        # add force from all other bodies
        for other in bodies:
            if other is not b:
                b.add_force(other)

   # update position
    for b in bodies:
        b.update(dt)


plt.plot(rx,ry)
    
