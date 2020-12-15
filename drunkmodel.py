#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:54:32 2020

@author: elliemarfleet
"""

# The algorithm for the model
# 1. Pull in the data file and finds out the pub point and the home points.
# 2. Draws the pub and homes on the screen.
# 3. Models the drunks leaving their pub and reaching their homes, and stores how many drunks pass through each point on the map.
# 4. Draws the density of drunks passing through each point on a map.
# 5. Saves the density map to a file as text.


# Import libraries needed for the model
import csv                      
import drunkframework           
import matplotlib.pyplot as plt


# Create the empty variable lists
density = []
environment = []
drunks = []
num_of_drunks = 25  # Known due to the increment of 10 from 10-250.


# Read in the town plan
# the plan is a 300 x 300 raster file representing 25 houses and 1 pub
# the pub is represented by 1s 
# Create a new text file to input the environment
f1 = open('drunk.plan.txt', newline='')
# Read in the csv with environment data
reader = csv.reader(f1, quoting = csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []                # create an empty list for rowlist to insert information into
    for value in row:
        rowlist.append(value)   # add the value to a rowlist
    environment.append(rowlist) # append the rowlist to the environment
f1.close()


## Check how the environment looks.
"""
plt.xlim(0, 300)
plt.ylim(0, 300)
plt.imshow(environment)
plt.show()
"""    


# Create the new density list from the environment text 
f2 = open('drunk.plan.txt', newline='')
# read in the csv with environment data
# change the value to 0 for an empty 2d list, which the agents alter as they walk over the coordinate
reader = csv.reader(f2, quoting = csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
        value = 0
        rowlist.append(value)
    density.append(rowlist)
f2.close()


# Find the pub location (signified by 1s in the environment)
# As the environment is a 2d list, read each row to find the 1s
# These points will be the starting coordinates for the drunks
for i, row in enumerate(environment):
    # For each number in that row
    for j, num in enumerate(row):
        # If the number equals 1 (the pub)
        if num == 1:
            start_x, start_y = j, i # assign number to the starting coordinates


# Create and move the drunks using a loop
# assign unique IDs which will be used to find their home
for i in range(num_of_drunks):
    drunk_ID = ((i+1)*10)  # because Python starts in 0 we have to add 1 first and then just multiply by 10
#   print(drunk_ID) # test IDs are right
    # Attach the drunks with the Class from drunkframework
    drunks.append(drunkframework.Drunk(density, drunk_ID, start_x, start_y))
    
    # While the coordinates of the drunks don't equal their home number
    while (environment[drunks[i].y][drunks[i].x] != drunks[i].drunk_ID):
        drunks[i].move()        # moves them
        drunks[i].add_density() # adds density to where they move
    # loop will stop once the drunk has found their home (i.e. their coordinates match their house number)
    print (environment[drunks[i].y][drunks[i].x], drunks[i].drunk_ID)


# Plot the density
# change the figure size and set the y and x-axis limits
plt.figure(figsize=(14,14))
plt.ylim(0, 300)
plt.xlim(0, 300)
# For the number of drunks, plot them on the density map
for i in range(num_of_drunks):
    plt.scatter(drunks[i].x,drunks[i].y, c="white", s=50)
plt.imshow(density)


## Plot to check if the model works
"""
plt.xlim(0,300)
plt.ylim(0,300)


plt.imshow(environment)
for i in range(num_of_drunks):
    plt.scatter(drunks[i].x,drunks[i].y)
plt.show()
"""


# Save the density map to a text file
with open('density.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in density:
        csvwriter.writerow(row)
        
   
        
"""
THE END
"""       
        