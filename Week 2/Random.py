# -*- coding: utf-8 -*-
"""
Created on 

@author: Quang
"""


"""
Numpy is a library support for lage, multi-dimensional arrays 
and matrices, along with a large collection of high-level 
mathematical function to operate on these array. 
"""
import numpy as np

list1 = ["handsome", "ugly"]
list2 = ["clever", "stupid"]
list3 = ["friendly","rude"] 


rand1 = np.random.randint(0,2)
rand2 = np.random.randint(0,2)
rand3 = np.random.randint(0,2)

print("\n" + "Quang is not only %s but also %s and %s" % (list1[rand1], list2[rand2], list3[rand3]))



