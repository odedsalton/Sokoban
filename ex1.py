import search
import random
import math


ids = ["203703467", "204375687"]

"""
*******************************************************************************************************************
Classes for help
*******************************************************************************************************************
"""

#
# class Spot:
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
#         return Spot(x, y)
#
#     def __str__(self):
#         return '(' + str(self.x) + ', ' + str(self.y) + ')'
#
#
# class Direction:
#     """ """
#
#     def __init__(self, spot, char):
#         self.spot = spot
#         self.char = char
#
#     def __str__(self):
#         return self.char
#
# """Global Directions"""
# R = Direction(Spot(1, 0), 'R')
# U = Direction(Spot(0, 1), 'U')
# L = Direction(Spot(-1, 0), 'L')
# D = Direction(Spot(0, -1), 'D')
#
#
# class State:
#     """class to represent a dynamic state of the board"""
#
#     def __init__(self, state):
#
#         pass


class Helper:
    """Helper functions"""

    def __init__(self):
        pass

    def findPlayer(self, state):
        for x, t in enumerate(state):
            for y, v in enumerate(t):
                if y in (17, 27, 37):
                    return x, y

    def canMove(self, state, x0, y0, x1, y1):
        # if coordinate in game
        if state[x1, y1]:
            # if a wall, not correct because still can move but nothing happens! (according to instructions)
            if state[x1, y1] == 99:
                return False
            # if there is box we need to check the next coordinate
            elif state[x1, y1] in (15, 35):
                return Helper.checkStone(state, x1 + (x1 - x0), y1 + (y1 - y0))
            return True
        return False

    def checkStone(self, state, x2, y2):
        # checks whether (x2,y2) is free to move a box to
        if state[x2, y2] in [10, 20, 30]:
            return True
        return False


"""
*******************************************************************************************************************
"""


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
        x, y = Helper.findPlayer(state)
        actions = []
        if Helper.canMove(state, x, y, x - 1, y):
            actions.append('L')
        if Helper.canMove(state, x, y, x + 1, y):
            actions.append('R')
        if Helper.canMove(state, x, y, x, y + 1):
            actions.append('U')
        if Helper.canMove(state, x, y, x, y - 1):
            actions.append('D')
        return tuple(actions)

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""

        x, y = Helper.findPlayer(state)

        new_state = ()

        return new_state

    def goal_test(self, state):
        """ Given a state, checks if this is the goal state.
         Returns True if it is, False otherwise."""
        not_allowed = [15, 20, 27, 35]
        for s in state:
            for w in s:
                if w in not_allowed:
                    # if any of those exists then there is a destination without box on it
                    return False
        return True

    def h(self, node):
        """ This is the heuristic. It gets a node (not a state,
        state can be accessed via node.state)
        and returns a goal distance estimate"""

    """Feel free to add your own functions"""


def create_sokoban_problem(game):
    return SokobanProblem(game)

























