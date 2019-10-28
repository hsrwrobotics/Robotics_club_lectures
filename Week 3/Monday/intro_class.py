# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 19:12:35 2019

HSRW Robotics
@author: mtc-20
"""
# A vehicle always has a color and wheels. We use this concept to create a 
# class Vehicle

# Class definition
class Vehicle():
    # preferably start with a constructor/initialization function that defines
    # the member variables
    def __init__(self, colour, wheels):
        self.color = colour
        self.wheels = wheels
    
    # a user defined function definition. Here we just print the description of 
    # the vehicle
    def get_desc(self):
        print ("This vehicle is %s and has %i wheels" %(self.color, self.wheels))
    # Also remember that all functions must have a self reference, which is the 
    # the first argument in every function call inside the class definition. 
    # Here we use self (which improves code readability, or use this), but it 
    # could be any other variable name      

# Creating an object of the Vehicle class
car = Vehicle("red", 4)

# We use the Vehicle class function to get the description
car.get_desc()

# Alternatively, you could again use user input to feed arguments.

# A question was raised during the session: the get_desc() function is 
# expecting an integer for wheels. How is it enforced?
# So, try this
any_vehicle = Vehicle(input("color: "),input("wheels"))
any_vehicle.get_desc() # Error?

# This is one way to rectify it
any_vehicle = Vehicle(input("color: "), int(input("wheels")))
any_vehicle.get_desc()

# The other way is to enforce the type inside the class definition itself