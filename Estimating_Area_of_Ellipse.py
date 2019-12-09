# Cynthia Cho
# DSC 430
# Due: February 5, 2019

# I have not given or received any unauthorized assistance on this assignment.


### Problem 2 ###


import random
import math

def ellipse():
    """Calculate the area of an ellipse using inputs for foci, length, and n number of random points."""

    print("Welcome!"+'\n'+"This program will use random numbers to compute the area of an ellipse.")
    ## assign values from input for F1x F1y for focus 1
    F1x, F1y= [float(x) for x in input("Enter the position of F1 (format: x y): ").split()]
    ## assign values from input for F2x F2y for focus 2
    F2x, F2y = [float(x) for x in input("Enter the position of F2 (format: x y): ").split()]
    length = eval(input("Enter the length of the major axis (format: l): "))
    ## user enters n number of random points to generate
    Rand_Points = eval(input("Enter the number of random points (format: n): "))

    
    left_bound = min(F1x,F2x) - length/2  ### defining left boundary
    right_bound = max(F1x,F2x) + length/2  ### defining right boundary
    bottom_bound = min(F1y,F2y) - length/2  ## defining bottom boundary
    top_bound = max(F1y,F2y) + length/2  ## defining top boundary

    rec_area = (abs(right_bound-left_bound))*(abs(top_bound -bottom_bound))  #calculate area of bounding box
    #print(rec_area)
    counter = 0  # initiate counter at 0
    for i in range(Rand_Points):  ## loops n number of time entered for random points
        x = random.uniform(left_bound,right_bound)  # x is the random x coordinate
        y = random.uniform(bottom_bound, top_bound)  # y is the random y coordinate
        ## x1 and x2 create a random point (x,y) 
        distance1 = math.sqrt((F1x-x)**2+(F1y-y)**2) ## calculate distance from point to focus 1
        distance2 = math.sqrt((F2x-x)**2+(F2y-y)**2)  ## calculate distance from point to focus 2
        dis_result = distance1 + distance2  ## sum distance from random point
        if dis_result <= length:  ## distance must be less than or equal than length to be within area of ellipse
            counter += 1  ## if within "area" of ellipse, counter adds value of 1
    Percent = counter / Rand_Points  ## caculates percentage of points that are within "area" of ellipse
    ellipse_area = rec_area* Percent  ## calculate the area of ellipse5
    print("Thinking…"+'\n'+"The area of the ellipse is approximately "+str(ellipse_area)+".")


##---------------------------------------------------------------------##
    
## Test function call:
ellipse()



## Below is what prints out when the function is called using the input from Assignment 2
'''
ellipse()
Welcome!
This program will use random numbers to compute the area of an ellipse.
Enter the position of F1 (format: x y): 2 4.5
Enter the position of F2 (format: x y): 3.6 -2
Enter the length of the major axis (format: l): 14
Enter the number of random points (format: n): 100000
Thinking…
The area of the ellipse is approximately 134.597424.
'''

