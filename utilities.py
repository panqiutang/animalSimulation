import random
import numpy as np

# map boundaries
MAP_MAX_X = 200
MAP_MAX_Y = 200


def moveOnce(oldpos, direction, length):
    newx = oldpos[0] + np.cos(direction)*length
    if newx < 0:
        newx = 0
    elif newx > MAP_MAX_X:
        newx = MAP_MAX_X
    newy = oldpos[1] + np.sin(direction)*length
    if newy < 0:
        newy = 0
    elif newy > MAP_MAX_Y:
        newy = MAP_MAX_Y

    return (newx, newy)
