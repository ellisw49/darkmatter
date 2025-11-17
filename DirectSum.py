#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 16:37:26 2025

@author: mwilliams
"""

# applying the integrator with direct summation

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

# call body.py
from Body import body 

# simuation parameters 

step = 50 # number of steps 
N = 1500   # number of bodies 
dt = 1e11  # time step 


# defining particle properties
mass = 2e31 # uniform mass in kg
color1 = "red"
windowsize = 3.086e16 # 1 kpc
vrange = 0.0# maximum velocity

# generate n 0bodies with initial positions and velocities
bodies = []
for n in range(N): 
    # rx = windowsize*(np.random.uniform())
    # ry = windowsize*(np.random.uniform())
    sigma = windowsize / 5   # about 0.2 pc core
    rx = np.random.normal(0, sigma)
    ry = np.random.normal(0, sigma)

    vx = vrange*(2*np.random.uniform()-1)  #normalized to 2*10^4
    vy = vrange*(2*np.random.uniform()-1) #normalized to 2*10^4
    
    b = body(rx, ry, vx, vy, mass, color1)
    bodies.append(b)


bodies = np.array(bodies)


# # for each time step
# for step in range(step):
    
    
#     # creating position arrays for plotting
#     rx_arr = []
#     ry_arr = []

#     # For each body in the system:
#     for b in bodies:
#         # reset force
#         b.resetforce()

#         # add force from all other bodies
#         for other in bodies:
#             if other is not b:
#                 b.addforce(other)

fig, ax = plt.subplots(figsize=(6,6),facecolor='black')
ax.set_facecolor("black")
scat = ax.scatter([b.rx for b in bodies], [b.ry for b in bodies], s=1, c='white')
ax.set_title("Direct N-body Simulation")


def update(frame):
    # 1. Reset forces
    for b in bodies:
        b.resetforce()
    
    # 2. Compute pairwise forces (direct summation)
    for i, b in enumerate(bodies):
        for j, other in enumerate(bodies):
            if i != j:
                b.addforce(other)
    
    # 3. Update positions
    for b in bodies:
        b.update(dt)
    
    # 4. Update scatter plot
    scat.set_offsets([[b.rx, b.ry] for b in bodies])
    ax.set_title(f"Timestep {frame}")
    return scat
    
ani = animation.FuncAnimation(fig, update, frames=step, interval=100, blit=False)

# 5. Save the animation as a GIF using PillowWriter
writer = animation.PillowWriter(fps=20, metadata=dict(artist='Me'), bitrate=1800)
ani.save("test.gif",writer=writer)
plt.show()


   # # update position and velocity (advancing 1 time step)
   #  for b in bodies:
   #      b.update(dt)
        
   #      rx_arr.append(b.rx)
   #      ry_arr.append(b.ry)

   #  rx_arr = np.array(rx_arr)
   #  ry_arr = np.array(ry_arr)

   #  # show the plot of all bodies / add to movie 
   #  plt.scatter(rx_arr,ry_arr)
   #  plt.title(f"Timestep {step}")
   #  plt.show()
        
