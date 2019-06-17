import random

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
#
# # for a list of initial positions, move each position once by random
# def MoveOneStepMultiple(initial_positions, max_x, max_y, obstacles, olddirection):
#     directions = [0, 1, 2, 3]
#     newpositions = []
#     for i in range(len(initial_positions)):
#         x, y = initial_positions[i]
#         possible_directions = [0, 1, 2, 3]
#         possible_directions.remove(olddirection[i])
#         newdirection = random.choice(possible_directions)
#         if newdirection == 0: # east
#             newpositions.append((min(max_x, x + random.uniform(0, 2)), y))
#         if newdirection == 1: # south
#             newpositions.append((x, max(0, y - random.uniform(0, 2))))
#         if newdirection == 2: # west
#             newpositions.append((max(0, x - random.uniform(0, 2)), y))
#         if newdirection == 3: # north
#             newpositions.append((x, min(max_y, y + random.uniform(0, 2))))
#     return newpositions
#
# # move once by random
# def MoveOneStepOnce(initial_position, max_x, max_y, obstacles, olddirection):
#     newpositions = []
#     x, y = initial_positions
#     possible_directions = [0, 1, 2, 3]
#     possible_directions.remove(olddirection)
#     newdirection = random.choice(possible_directions)
#     if newdirection == 0: # east
#         return (min(max_x, x + random.uniform(0, 2)), y)
#     if newdirection == 1: # south
#         return (x, max(0, y - random.uniform(0, 2)))
#     if newdirection == 2: # west
#         return (max(0, x - random.uniform(0, 2)), y)
#     if newdirection == 3: # north
#         return (x, min(max_y, y + random.uniform(0, 2)))
#
# if __name__ == "__main__":
#     initial_positions = [(1, 2), (0, 0), (8, 1)]
#     print(MoveOneStepMultiple(initial_positions, 9, 9, [], [0, 3, 2]))
