# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:45:23 2019

HSRW Robotics
@author: mtc-20
"""

import game_objects as go
#import game_actions
from game_actions import get_input
import time

try:
    go.create_player(input("Enter name: "), input("Choose a class(elf, goblin): "))
    enemy = go.Goblin('Hobgob')
    foe = go.Elf('Etherea')
    while True:
        #game_actions.get_input()
        get_input()
        time.sleep(1)
        
#except NameError:
#    print ("Game Over")
     
except Exception as e:
    print("Interrupted", type(e),'\n', e)


#go.create_player(input("Enter name: "), input("Choose a class(elf, goblin): "))
#enemy = go.Goblin('Hobo')    
#while True:
#    try:
#        get_input()
#    
#    except Exception as e:
#        print("Game closed. \n Reason:", type(e), e)