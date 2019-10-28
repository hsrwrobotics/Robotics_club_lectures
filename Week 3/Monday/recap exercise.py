# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:39:01 2019

HSRW Robotics
@author: mtc-20
"""
# The safe and robust approach. A function that returns True or False and 
# doesn't store the preset value any variable that can be accessed or modified

#function definition
def password(user_input):
    if user_input == "123456":
        #print("Input password is right. Proceed...")
        return True
    else: 
        #print("Incorrect password. Shutting Down!")
        return False

#function call    
password(input("Enter password: "))
password(123456) # Did this work as predicted???

# The 'smart' approach. A function behaves exactly as the above function but
# requires only 1 line of definition
def password2(user_input):
    return user_input == "123456"

password2(input("Enter password: "))

# The 'cool' approach. A function that doesn't require a separate definition
# and call, but still behaves alike. Drawback: not exactly re-usable
print((lambda user_input: user_input=="123")(input("Enter password: ")))

# Make it reusable by declaring as so
password3 = (lambda user_input: user_input=="123")
print (password3(input("Enter password: ")))

# Additionally to check both user and password, make use of logical operations
def usr_password(name, key):
    return (name=="Tom" and key =="123")

usr_password(input("Name: "),input("key: "))