# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 10:37:12 2025

@author: iruch
"""

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

# call body.py
from Body2 import body 

# initializing the bodies in a normal distribution for testing
def makebodies_test(N):
    
    # generate n bodies with specified initial positions and velocities
    
    # defining particle properties
    mass = 1 # uniform mass in solar masses
    color1 = "red"
    windowsize = 10 # AU
    vrange = 0.0 # maximum velocity
    
    bodies = []
    
    rng = np.random.default_rng(seed=42)   # <-- moved outside the loop

    for n in range(N):
        rx = rng.normal(0, 5)
        ry = rng.normal(0, 5)
        vx = rng.normal()
        vy = rng.normal()

        b = body(rx, ry, vx, vy, mass, color1)
        bodies.append(b)

        
    return bodies


# # defining universal animation protocall
# def ani_setup():
#     fig, ax = plt.subplots(figsize=(6,6),facecolor='black')
#     ax.set_facecolor("black")
#     scat = ax.scatter([b.rx for b in bodies], [b.ry for b in bodies], s=1, c='white')
#     ax.set_title("N-body Simulation")
    
    
    
