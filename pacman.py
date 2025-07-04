# pacman.py
# this file contains a class to creat Pac-Man


class PacMan:
    def __init__(self, pos):
        """All Pac-Man needs for initialization is a starting position."""
        self.pos = pos

    def move(self, direction, maze):
        """
        Moves Pac-Man in the given direction if not blocked by a wall.
        Directions:
        (1,0) = right
        (-1,0) = left
        (0,1) = up
        (0,-1) = down
        """
        x, y = self.pos
        dx, dy = direction
        new_pos = (x + dx, y + dy)

        if maze.in_bounds(new_pos) and maze.passable(new_pos):
            self.pos = new_pos
