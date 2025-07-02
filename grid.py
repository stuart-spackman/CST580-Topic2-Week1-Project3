# grid.py
# this file contains the maze grid, walls, and valid moves

# imports
import numpy as np


class MazeGrid:
    def __init__(self, width, height, walls):
        self.width = width
        self.height = height
        self.walls = set(walls)  # a set can be used for faster lookup

    def in_bounds(self, pos):
        """
        We need to be able to check if a position is within the maze dimensions.
        """
        x, y = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, pos):
        """
        We also need to be able to check is a position is not a wall.
        """
        return pos not in self.walls

    def neighbors(self, pos):
        """
        Return valid neighboring positions from a given tile.
        """
        x, y = pos
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # right, left, up, down
        result = [(x + dx, y + dy) for dx, dy in directions]
        return [p for p in result if self.in_bounds(p) and self.passable(p)]
