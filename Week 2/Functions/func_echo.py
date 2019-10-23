# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:15:36 2019

HSRW Robotics
@author: mtc-20
"""

# A function definition starts with the keyword def followed the function
# name which can be anything starting with an alphabet, preferably in
# lowercase followed by a colon {:}. The body(the block of code to be reused)
# starts in the subsequent line and is closed by the return statement
# Below is a simple function that takes 0 arguments and returns nothing
def echo():
    shoutout = input("Shout out something: ")
    print(shoutout.upper())
    print(shoutout)
    print(shoutout.lower())
    for i in range(len(shoutout)):
        print(shoutout[:-i].lower())
    return

# To use the function, it can be called in different ways:
echo()
test_echo = echo()
print ("\n", test_echo)

# Pay attention to the variable explorer, is there anything stored?
# What about the print statements from the different call?



# Below is another way of writing the same function. Functions can also have
# arguments that are passed in brackets {()}. Arguments are variables and a
# function can have any number of arguments. 
# The below function takes 1 argument and returns True value always
def echo2(shoutout):
    print(shoutout.upper())
    print(shoutout)
    print(shoutout.lower())
    for i in range(len(shoutout)):
        print(shoutout[:-i].lower())
    return True

# There are atleast 3 different ways to call this function, that's your task
