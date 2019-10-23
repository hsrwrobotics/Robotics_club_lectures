# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:15:36 2019

HSRW Robotics
@author: mtc-20
"""
# Use a variable to store the input string
string = input("Shout out something: ")

# This is like a confirmation check stating what is going to be
# echoed to cross check th input
print("Echoing ", string)

# Use .upper() to print the input in all uppercase.
print (string.upper())
print(string)
print(string.lower())

# Expicitly specify how much of the input to be printed.
print(string[:-1])
print(string[0:-2])

# Now if we want this to be repeated again, we would have to type/copy
# the same 7 lines again and again, which is just redundant and tiring