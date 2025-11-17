#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 18:22:09 2025

@author: mwilliams
"""

import numpy as np

class body:
    
    # defining class-wide variables G and solar mass
    G = 6.673e-11
    solarmass=1.98892e30
    
    # initializing body object with position, velocity, mass, color
    def  __init__(self, rx, ry, vx, vy, mass, color):
        
        # positions 
        self.rx = rx
        self.ry = ry
        
        # velocities 
        self.vx = vx
        self.vy = vy
        
        # mass and color
        self.mass = mass
        self.color = color
        
        # inital force accumulation 
        #self.fx = 0.0
        #self.fy = 0.0
       
        
    # distance_to calculates the distance between this body and other body
    def distance_to(self, other):
        
        dx = self.rx - other.rx
        dy = self.ry - other.ry
        return np.sqrt(dx **2 + dy **2)
    
    # zeroing force between iterations
    def resetforce(self):
        self.fx = 0.0
        self.fy = 0.0
        
    # calculating the force between this body and other body
    def addforce(self,other):
        
        G = 6.673e-11
        # calculating distance between the particles
        dx = other.rx - self.rx
        dy = other.ry - self.ry
        dist = np.sqrt(dx**2 + dy**2)
        # calculating gravitational force
        f = G * (self.mass * other.mass) / (dist**2)
        # adding this force to this body
        
        # self.fx += f * dx / dist    # Fcos(theta) = f * dx/dist
        # self.fy += f * dy / dist  
        self.fx -= f * np.cos(np.arctan(dy/dx))
        self.fy -= f *np.sin(np.arctan(dy/dx))
   
    # update method completes one time step
    def update(self,dt): 
        
        '''
        vx += dt * fx / mass
        vy += dt * fy / mass
        rx += dt * vx
        ry += dt * vy
        return vx, vy, rx, ry
        '''
        # calc acceleration from force/mass
        ax = self.fx/self.mass  
        ay = self.fy/self.mass 
        
        
        # EULER
        
        # update velocity w/ acceleration and dt
        self.vx += ax*dt        
        self.vy += ay*dt 
        
        # update positions w/ vdt 
        self.rx += self.vx *dt  
        self.ry += self.vy *dt 
        
        # RK4 (pseudocode)
        
        
         
        k1x  = dt * self.fx / self.mass
        k1y = dt * self.fy / self.mass 
        
        k2x =  dt * (self.fx + k1x / 2) / self.mass
        k2y =  dt * (self.fy + k1y / 2) / self.mass
        
        k3x = dt * (self.fx + k2x / 2 ) / self.mass
        k3y = dt * (self.fy + k2y / 2 ) / self.mass
        
        k4x = dt * (self.fx + k3x) / self.mass
        k4y = dt * (self.fy + k3y) / self.mass
        
        self.rx = self.rx + (k1x + 2* k2x )
        
        
        
        
        # a2x = f2x / m
        # a2y = f2y / m
     
        # k2 = k2 formula
        
        # calculate force 3
         
        # a3x = f3x / m
        # a3y = f3y / m
     
        # k3 = k3 formula
        
        # calculate force 4
         
        # a4x = f4x / m
        # a4y = f4y / m
     
        # k4 = k4 formula
        
        
    
    # putting all of the number variables in a string
    def tostring(self):
        return f"Body(rx={self.rx: .3f}, ry={self.ry:.3f}, vx={self.vx:.3f}, vy={self.vy:.3f}, m={self.mass:.3f})"

    # checking what quadrant this body is in
    def inquad(self,q):
        return q.contains(self.rx,self.ry)
    

    
