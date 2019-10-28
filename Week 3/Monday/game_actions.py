# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:14:38 2019

@author: Wolf
"""
from game_objects import GameObject

def examine(noun):
    if noun.lower() in GameObject.objects:
        return GameObject.objects[noun.lower()].get_desc()
    else:
        return ("There is no %s here." %noun)
    
def say(noun):
    noun = " ".join(noun)
    return ("Player said {}".format(noun))
    
def get_input():
    command = input('Input your command here(say, examine, hit):').split()
    verb_word = command[0].lower()
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown command: {}".format(verb_word))
        return
    
    if len(command) ==2:
        noun_word = command[1]
        print (verb(noun_word))
    elif len(command) > 2 and verb_word == 'say':
        noun_word = command[1:]
        print (verb(noun_word))
    else:
        print(verb('Nothing'))
        return

def hit(noun):
    if noun.lower() in GameObject.objects:
        thing = GameObject.objects[noun.lower()]
        thing.health = thing.health - 1
        if thing.health <= 0:
            status = "You killed the %s!" %(thing.class_name.lower())
        else:
            status = "You hit the %s" %(thing.class_name.lower())
                
    else:
        return ("There is no %s here" %(noun.lower()))
    return status
            
        
verb_dict = {'say': say, 'examine':examine, 'hit':hit}