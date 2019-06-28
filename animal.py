import random
import math
import time
import numpy as np
import matplotlib.pyplot as plt

from stimuli import *
from utilities import *

# Base class for all animals
class Animal:
    def __init__(self, location):
        self.location = location
        self.direction = random.uniform(0, math.pi*2)
        self.stride = 2
        self.Need = Need()
        self.state = "idle"
        self.prey = True # if I am a prey to other animals

    # Actions
    def eat(self):
        self.state = "eat"
        # assume grass is everywhere so the zerba can eat whenever is hungry
        self.Need.Hunger.hunger = min(100, self.Need.Hunger.hunger + 5)

    def sleep(self):
        self.state = "sleep"
        self.Need.Tired.tiredness -= 5

    # Low level actions
    def idle(self):
        self.state = "idle"
        newdirection = random.uniform(0, math.pi*2)
        self.location = moveOnce(self.location, newdirection, self.stride)
        self.direction = newdirection

    # TODO: lay, walk, stand up
    def consumeOneTimeStep(self):
        if self.state == "dead":
            return

        self.Need.Hunger.hunger -= 1
        self.Need.Tired.tiredness += 1

        if self.prey:
            predators = animals['lion']
            predator = predators[0]
            distance = math.hypot(self.location[0] - predator.location[0], self.location[1] - predator.location[1])
            if distance <= self.stride: # been caught
                self.die()
                return
            elif distance <= 10: # hasn't been caught; only flees when predator is within 10 steps away
                self.state = "flee"
                direction = math.atan2(predator.location[1] - self.location[1], predator.location[0] - self.location[0])
                self.direction = direction + math.pi
                self.location = moveOnce(self.location, self.direction, self.stride)
                return

        if self.Need.Tired.isTired():
            self.sleep()
        elif self.Need.Hunger.isHungry():
            self.eat()
        else:
            self.idle()


    def die(self):
        self.state = "dead"


class Need:
    def __init__(self):
        self.Hunger = Need.Hunger()
        self.Tired = Need.Tired()

    class Hunger:
        def __init__(self):
            self.hunger = 100 # How hungry the animal is. 100 means full
            self.priority = 1 # Highest level of priority

        # return a boolean; if the animal is hungry or not
        def isHungry(self):
            return self.hunger <= 95

    class Tired:
        def __init__(self):
            self.tiredness = 0
            self.priority = 1

        def isTired(self):
            return self.tiredness >= 5


class Zebra(Animal):
    def __init__(self, location):
        Animal.__init__(self, location)


class Lion(Animal):
    def __init__(self, location):
        Animal.__init__(self, location)
        self.stride = 5
        self.prey = False

    def chase(self):
        preys = animals['zebra']
        # choose the most convenient prey
        prey = preys[0]

        distance = math.hypot(self.location[0] - prey.location[0], self.location[1] - prey.location[1])
        if distance <= self.stride: # caught the prey
            self.location = prey.location
            prey.die()
            return True
        else: # didn't catch the prey
            self.state = "chase"
            direction = math.atan2(prey.location[1] - self.location[1], prey.location[0] - self.location[0])
            self.location = moveOnce(self.location, direction, self.stride)
            self.direction = direction
            return False

    def eat(self):
        if self.chase():
            self.Need.Hunger.hunger = min(100, self.Need.Hunger.hunger + 50)


def log(animal, file, timestep):
    file.write("Timestep: {},".format(timestep))
    file.write("location: {},".format(animal.location))
    file.write("direction: {},".format(animal.direction))
    file.write("state: {},".format(animal.state))
    file.write("hunger: {},".format(animal.Need.Hunger.hunger))
    file.write("tiredness: {}".format(animal.Need.Tired.tiredness))
    file.write("\n")


if __name__=="__main__":
    # map of types to animal objects
    animals = {}
    location1 = (100, 100)
    zebra1 = Zebra(location1)
    location2 = (150, 100)
    lion1 = Lion(location2)
    animals['zebra'] = [zebra1]
    animals['lion'] = [lion1]

    f1 = open('zebra1.txt', 'w+')
    f2 = open('lion1.txt', 'w+')
    zebra1x = []
    zebra1y = []
    lion1x = []
    lion1y = []

    for timestep in range(30):
        print(timestep)
        zebra1.consumeOneTimeStep()
        log(zebra1, f1, timestep)
        zebra1x.append(zebra1.location[0])
        zebra1y.append(zebra1.location[1])

        lion1.consumeOneTimeStep()
        log(lion1, f2, timestep)
        lion1x.append(lion1.location[0])
        lion1y.append(lion1.location[1])


    plt.plot(zebra1x, zebra1y)
    plt.savefig('zebra.png')
    plt.plot(lion1x, lion1y)
    plt.savefig('lion.png')
