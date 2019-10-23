# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:15:36 2019

HSRW Robotics
@author: mtc-20
"""
# Factorial of a number n {n!} is given by 
# n! = n * (n-1)!
# n! = n * (n-1) * (n-2)!
# .
# .
# .
# n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
# Using recursion, this can be written in just 2 lines of code

def factorial(no):
    if no > 0:
        return no * fact(no - 1)
    else:
        return 1

print ("Factorial is" , factorial(int(input("Enter a positive number: "))))
