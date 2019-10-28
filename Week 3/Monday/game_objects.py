# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:13:40 2019

@author: Wolf
"""

class GameObject:
    class_name = ""
    desc = ""
    objects = {}
    def __init__(self,name):
        self.name = name
        GameObject.objects[self.class_name] = self
    
    def get_desc(self):
        return self.name + "\n"+ self.class_name + "\n" + self.desc
    
class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self._desc = "A foul creature"
        self.health = 3
        self.profile = "goblin.jpg"
        super().__init__(name)
    
    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            status = "It has minor wounds and is angry."
        elif self.health == 1:
            status = "It has serious injury and is exhausted."
        elif self.health <= 0:
            status = "It is dead."
        return status
    
class Elf(GameObject):
    def __init__(self, name):
        self.class_name = "elf"
        self._desc = "A powerful being"
        self.health = 5
        super().__init__(name)
    
    @property
    def desc(self):
        if self.health >= 5:
            return self._desc
        elif self.health >= 3:
            status = "It has minor wounds and is angry."
        elif self.health == 1:
            status = "It has serious injury and is exhausted."
        elif self.health <= 0:
            status = "%s is dead." % self.name
            raise NameError
        return status

class Player(GameObject):
    def __init__(self, name, class_name):
        self.class_name = "self"
        self._desc = "An anomaly"
        self.health = 1
        super().__init__(name)
    
    @property
    def desc(self):
        if self.health >= 5:
            return self._desc
        elif self.health >= 3:
            status = "It has minor wounds and is angry."
        elif self.health == 1:
            status = "It has serious injury and is exhausted."
        elif self.health <= 0:
            status = "Player is dead."
            print (status)
            raise NameError
        return status
    
    

def create_player(name, class_name):
    if class_name.lower() == 'goblin':
        return Goblin(name)
    elif class_name.lower() == 'elf':
        return Elf(name)
    else:
        return Player(name, class_name)

