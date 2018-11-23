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
        player_index = Helper.findPlayer(state)
        x, y = player_index[0], player_index[1]
        left = Helper.canMove(state, x, y, x - 1, y)
        right = Helper.canMove(state, x, y, x + 1, y)
        up = Helper.canMove(state, x, y, x, y + 1)
        down = Helper.canMove(state, x, y, x, y - 1)
        actions = {'L': left, 'U': up, 'R': right, 'D': down}
        return tuple(actions.values())

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        player_index = Helper.findPlayer(state)
        x, y = player_index[0], player_index[1]

        new_state = ()

        return new_state


    def goal_test(self, state):
        """ Given a state, checks if this is the goal state.
         Returns True if it is, False otherwise."""

    def h(self, node):
        """ This is the heuristic. It gets a node (not a state,
        state can be accessed via node.state)
        and returns a goal distance estimate"""

    """Feel free to add your own functions"""


def create_sokoban_problem(game):
    return SokobanProblem(game)


class Helper:
    """Helper functions"""

    def __init__(self):
        pass

    def findPlayer(self, state):
        for s in state:
            for w in s:
                if w in (17, 37):
                    x = s.index(w)
                    y = state.index(s)
                    return (x, y)

    def canMove(self, state, x0, y0, x1, y1):
        if state[x1, y1] in (None, 99):
            return 0
        elif state[x1, y1] in (15, 35):
            return Helper.canMove(state, x1, y1, x1 + (x1 - x0), y1 + (y1 - y0))
        return 1

# if state[x1, y1] in (99, None):
        #     return False
        # elif state[x1, y1] in (15, 35):
        #     if state[x2, y2] in (99, 35, 15, None):
        #         return False
        #     return True
        # return True




