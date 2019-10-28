# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:54:48 2019

HSRW Robotics
@author: mtc-20
"""
# Syntax errors
print 10

#Execution errors
test = 10*1/0 

print ("SPAM".lower)

# try except block that simply passes past the error without any error message
try:
    print(10/0)
    
except:
    pass

# except block to find out the type of error caught
try:
    print(10/0)
    # print (spam) #test the code with this as well to see the output
except Exception as e:
    print("Caught exception:", e)
    print(type(e))

# except block that catches only one type of error (the ZeroDivisionError in 
# this case)
# Also note you can have multiple except blocks
try:
    print (spam)

except ZeroDivisionError:
    print("1")
#except:
#    pass

except:
    print ("Interrupted!")
   
    
# you could also create your own type of error as derived classes of Exception
# but that won't be covered here
