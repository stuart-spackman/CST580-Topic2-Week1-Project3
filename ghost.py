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
        # print(f"Ghost at {self.pos} planning path to {target}")

        self.path = a_star_search(self.pos, target, maze)
        # print(f"Planned path: {self.path}")

        # move one step along the path if possible
        if self.path and len(self.path) > 1:
            self.pos = self.path[1]
