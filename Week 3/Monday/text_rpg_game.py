# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:45:23 2019

@author: Wolf
"""

import game_objects
import game_actions
import time

try:
    game_objects.create_player(input("Enter name: "), input("Choose a class(elf, goblin): "))
    enemy = game_objects.Goblin('Hobgob')
    while True:
        game_actions.get_input()
        time.sleep(1)
        
except NameError:
    print ("Game Over")
    
    
except Exception as e:
    print("Interrupted", type(e),'\n', e)