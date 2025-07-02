# ghost.py
# this file contains the ghost logic
# this includes HMM + A*

# imports
from pathfinding import a_star_search


class Ghost:
    def __init__(self, start_pos):
        self.pos = start_pos  # current position of the ghost
        self.path = []  # current planned path

    def update(self, belief_state, maze):
        """
        We need a method for updating ghost behavior:
        1. Determine most likely location of Pac-Man
        2. Use A* to move one step toward that target
        """
        target = belief_state.most_likely_position()
        self.path = a_star_search(self.pos, target, maze)

        # move one step along the path if possible
        if self.path:
            self.pos = self.path[0]
