import search
import random
import math


ids = ["203703467", "204375687"]


class SokobanProblem(search.Problem):
    """This class implements a sokoban problem"""

    def __init__(self, initial):
        """Don't forget to implement the goal test
        You should change the initial to your own representation"""
        search.Problem.__init__(self, initial)

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a tuple, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        player = findPlayer(state)
        actions = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}
        for key, val in actions.items():
            if not checkDirection(state, player, val):
                actions.pop(key)
        return tuple(actions.keys())

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        direction = ()
        if action is 'U':
            direction = (0, 1)
        elif action is 'D':
            direction = (0, -1)
        elif action is 'L':
            direction = (-1, 0)
        else:
            direction = (1, 0)

        return Move(state, findPlayer(state), direction)

    def goal_test(self, state):
        """ Given a state, checks if this is the goal state.
         Returns True if it is, False otherwise."""
        not_allowed = [15, 20, 27, 35]
        for s in state:
            for w in s:
                if w in not_allowed:
                    # if any of those exists then there is a destination without box on it - Game NOT-Over
                    return False
        # Game-Over
        return True

    def h(self, node):
        """ This is the heuristic. It gets a node (not a state,
        state can be accessed via node.state)
        and returns a goal distance estimate"""

    """Feel free to add your own functions"""


def create_sokoban_problem(game):
    return SokobanProblem(game)


"""
************************************************************************************************************************ 
----------------------------------------------- More Functions ---------------------------------------------------------
************************************************************************************************************************
"""


def findPlayer(state):
    for x, t in enumerate(state):
        for y, v in enumerate(t):
            if y in (17, 27, 37):
                return x, y


def checkDirection(state, index, direction):
    can_move = [10, 20, 30]
    boxes = [15, 25, 35]
    index += direction
    # check if in bounds
    if index in (range(0, len(state)), range(0, len(state[0]))):
        # check if clear to move
        if (index in can_move) or ((index in boxes) and (index+direction in can_move)):
            return True
    return False


def Move(state, player, direction):
    new_state = []
    return tuple(new_state)












#
# """
# *******************************************************************************************************************
# Classes for help
# *******************************************************************************************************************
# """
#
#
# class Dot:
#
#     """ Coordinate object """
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         if (self.x, self.y) == (other.x, other.y):
#             return True
#         return False
#
#     def __add__(self, other):
#         x, y = self.x + other.x, self.y + other.y
#         return Dot(x, y)
#
#     def __str__(self):
#         return '(' + str(self.x) + ', ' + str(self.y) + ')'
#
#     def __hash__(self):
#         return hash((self.x, self.y))
#
#
# class Direction:
#     """ Direction object """
#
#     def __init__(self, dot, char):
#         self.dot = dot
#         self.char = char
#
#     def __str__(self):
#         return self.char
#
# """Global Directions"""
# R = Direction(Dot(1, 0), 'R')
# U = Direction(Dot(0, 1), 'U')
# L = Direction(Dot(-1, 0), 'L')
# D = Direction(Dot(0, -1), 'D')
#
#
# def findPlayer(state):
#     for x, t in enumerate(state):
#         for y, v in enumerate(t):
#             if y in (17, 27, 37):
#                 return x, y
#
#
# def checkDirection(state, player, direction):
#     index = player + direction
#     if index in (range(0, len(state)), range(0, len(state[0]))):
#         if index in [10, 20, 30]:
#             return True
#         if index in [15, 25, 35]:
#             return checkDirection(state, index, direction)
#     return False

#
# class Helper:
#     """Helper functions"""
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def findPlayer(state):
#         for x, t in enumerate(state):
#             for y, v in enumerate(t):
#                 if y in (17, 27, 37):
#                     return x, y
#
#     @staticmethod
#     def canMove(state, x0, y0, x1, y1):
#         # if coordinate in game
#         if state[x1, y1]:
#             # if a wall, not correct because still can move but nothing happens! (according to instructions)
#             if state[x1, y1] == 99:
#                 return False
#             # if there is box we need to check the next coordinate
#             elif state[x1, y1] in (15, 35):
#                 return Helper.checkStone(x1 + (x1 - x0), y1 + (y1 - y0))
#             return True
#         return False
#
#     @staticmethod
#     def checkStone(state, x2, y2):
#         # checks whether (x2,y2) is free to move a box to
#         if state[x2, y2] in [10, 20, 30]:
#             return True
#         return False







