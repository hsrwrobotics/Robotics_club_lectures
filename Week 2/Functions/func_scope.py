# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:15:36 2019

HSRW Robotics
@author: mtc-20
"""

# Variables declared inside a function are called local variables. These exist
# only within the "scope" of the function.

# The 2 functions below are quite similar except for just one line of code
# Refer to the variable explorer to figure out what is happening with local and
# global variables

def changeme(mylist):
    mylist = [1,2,3]
    print ("values inside the function: ", mylist)
    return 

def includeme(mylist):
    mylist.append([1,2,3])
    print ("values inside the function: ", mylist)
    return 



# Initialize a list with the same name as the argument in the function def
mylist = [10,20,30]

changeme(mylist)
print("values outside the function: ", mylist)

mylist = [10,20,30]
includeme(mylist)
print("values outside the function: ", mylist)

includeme(mylist)

# Here's another example if you quite haven't figured out how local variables
# and return statements work. Run the below code as is first, then commment out
# the empty return statement{line 49} and uncomment the others {Lines 49, 55
# and 56}. Now run this, do you notice the difference?

def changeme(mylist):
    local_var = "Just a test"
    mylist = [1,2,3]
    print ("values inside the function: \n mylist= ", mylist)
    print ("local_var= ", local_var)
    return
    ##return local_var 
    

changeme(mylist)
print (local_var)

##var = changeme(mylist)
##print(var)
