#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:55:17 2020

@author: elliemarfleet
"""

# Import libraries needed for the model
import random


# Create the drunk class
class Drunk:
    # create the agents and their attributes
    def __init__(self, density, drunk_ID, start_x, start_y):
        self.x = start_x            # starting coordinates from the pub
        self.y = start_y            # starting coordinates from the pubs
        self.drunk_ID = drunk_ID    # drunk_ID defined in the model, assigns number to drunks to find their home
        self.alcohol_levels = 100   # starting alcohol levels, changes the way they move
        self.density = density      # used for creating density definition
    
    
# Move the drunks dependent on different conditions
    def move(self):
        # If the person is drunk, make their movement staggered by moving at random integers between 1-3
        # % is a torus boundary in order to keep the drunks inside the defined environment
        if self.alcohol_levels > 0:
            if random.random() < 0.5:
                self.x = (self.x + (random.randint(1,3))) % 300    # if random number is <0.05, add 1 to the x axis of the agent
            else:
                self.x = (self.x - (random.randint(1,3))) % 300    # if random number is >0.05, subtract 1 to the x axis of the agent
            if random.random() < 0.5:
                self.y = (self.y + (random.randint(1,3))) % 300    # if random number is <0.05, add 1 to the y axis of the agent
            else:
                self.y = (self.y - (random.randint(1,3))) % 300    # if random number is >0.05, subtract 1 to the y axis of the agent
                
        if self.alcohol_levels == 0: # when the drunk's alcohol level is 0, stop staggering
            if random.random() < 0.5:
                self.x = (self.x + 1) % 300 # if random number is <0.05, add 1 to the x-axis of the agent
            else:
                self.x = (self.x - 1) % 300 # if random number is >0.05, subtract 1 to the x-axis of the agent
            if random.random() < 0.5:
                self.y = (self.y + 1) % 300 # if random number is <0.05, add 1 to the y-axis of the agent
            else:
                self.y = (self.y - 1) % 300 # if random number is >0.05, subtract 1 to the y-axis of the agent
    
    
# Method to monitor density   
    def add_density(self):
        # Add 1 to the density list with the drunk location
        self.density[self.x][self.y] += 1  
        


 

        
        
        
        