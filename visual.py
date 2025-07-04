# visual.py
# this file sets up the necessary visuals for showing the game take place
# in pygame

# imports
import pygame
import numpy as np

# each tile in the grid will be 40x40 pixels
TILE_SIZE = 40

# colors (RGB)
WALL_COLOR = (50, 50, 50)  # dark gray
EMPTY_COLOR = (230, 230, 230)  # light gray
GHOST_COLOR = (255, 50, 50)  # red
BELIEF_BASE_COLOR = (50, 50, 255)  # blue
PACMAN_COLOR = (255, 255, 0)  # yellow


def draw_grid(screen, maze, belief, ghost, pacman):
    """
    Draws the maze grid, walls, belief heatmap, and the ghosts's position.
    """
    for x in range(maze.width):
        for y in range(maze.height):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

            # draw wall tiles
            if (x, y) in maze.walls:
                pygame.draw.rect(screen, WALL_COLOR, rect)
            else:
                # draw empty floor tile
                pygame.draw.rect(screen, EMPTY_COLOR, rect)

                # shade based on belief state
                if belief:
                    prob = belief.belief[x, y]

                    # increase shading intensity
                    shade = min(int(prob * 255 * 20), 255)

                    # decrease R and G components
                    # this will make the tile more blue
                    r = max(0, EMPTY_COLOR[0] - shade)
                    g = max(0, EMPTY_COLOR[1] - shade)
                    b = EMPTY_COLOR[2]  # leave blue unchanged
                    color = (r, g, b)

                    pygame.draw.rect(screen, color, rect)

            # draw grid border
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)

    # draw ghost as a red circle
    gx, gy = ghost.pos
    rect = pygame.Rect(gx * TILE_SIZE, gy * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.ellipse(screen, GHOST_COLOR, rect)

    # draw Pac-Man as a yellow circle
    px, py = pacman.pos
    rect = pygame.Rect(px * TILE_SIZE, py * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.ellipse(screen, PACMAN_COLOR, rect)
