import random
import math
import time
import numpy

from stimuli import *
from utilities import *

# Base class for all animals
class Animal:
    def __init__(self, location):
        self.location = location # (x, y)
        self.direction = random.uniform(0, math.pi*2)
        self.stride = 2
        self.Need = Need()

    # Actions
    def eat(self):
        self.Need.Hunger.hunger = min(100, self.Need.Hunger.hunger + 5)

    def sleep(self):
        time.sleep(5)
        pass

    # Low level actions
    def idle(self):
        newdirection = random.uniform(0, math.pi*2)
        self.location = moveOnce(self.location, newdirection, self.stride)


    # TODO: lay, walk, stand up


class Need:
    class Hunger:
        def __init__(self):
            self.hunger = 100 # How hungry the animal is. 100 means full
            self.priority = 1 # Highest level of priority

        # return a boolean; if the animal is hungry or not
        def isHungry(self):
            return self.hunger <= 50

    class Tired:
        def __init__(self):
            self.tiredness = 0
            self.priority = 1

        def isTired(self)
            return self.tiredness >= 50
    # TODO: flee

class Zebra(Animal):
    def __init__(self):
        Animal.__init__(self)


class Lion(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.stride = 3

    def eat(self):
        if chase(self):
            self.Need.Hunger.hunger = min(100, self.Need.Hunger.hunger + 50)

    def chase(self):
        preys = get_animal_locations("zebra")
        # choose the most convenient prey
        prey = preys[0]
        distance = math.hypot(self.location[0] - prey[0], self.location[1] - prey[1])
        if distance <= self.stride: # caught the prey
            self.location = prey.location
            return True
        else: # didn't catch the prey
            direction = math.atan2(prey[1] - self.location[1], prey[0] - self.location[0])
            self.location = moveOnce(self.location, direction, self.stride)
            self.direction = direction
            return False
