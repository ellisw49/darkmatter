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

N = 1 # number of bodies
dt = 1 # time step in seconds
step = 1 # number of steps

# defining particle properties

mass = 1.0 # uniform mass in kg
color = "red"
windowsize = 3.086e22 # 1 Mpc
vrange = 2e4 # maximum velocity

bodies = []
    for n in range(N):
        rx = windowsize * np.random.uniform()
        ry = windowsize * np.random.uniform()
        vx = vrange * np.random.uniform()
        vy = vrange * np.random.uniform()


# initialize code to make movie

# create new bhtree for all bodies on the screen

# for all bodies in the tree:
    
    # reset force to zero
    
    # if bodies in q:
    
        # update force
        
        # update positions by 1 time step
        
        # update plot / movie / graphic for all bodies