# main.py
# this file contains the game's simulation loop

# imports
import pygame
import sys
from grid import MazeGrid
from ghost import Ghost
from pacman import PacMan
from belief import BeliefState
from visual import draw_grid

# set maze configuration
WIDTH, HEIGHT = 10, 10  # maze grid size (10x10)
FPS = 5  # controls simulation speed (frames per second)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH * 40, HEIGHT * 40))  # window size
pygame.display.set_caption("Pac-Man HMM Ghost AI")
clock = pygame.time.Clock()

# maze setup
walls = [(5, 5), (5, 6), (5, 7)]  # wall tiles
maze = MazeGrid(WIDTH, HEIGHT, walls)

# create game entities
ghost = Ghost(start_pos=(0, 0))  # ghost starts in upper left
belief = BeliefState(WIDTH, HEIGHT)
pacman = PacMan(pos=(8, 8))

# simulated "true" Pac-Man location
true_pacman_pos = (8, 8)


def fake_observation():
    """
    Fake observations might be useful for testing purposes.
    Here we simulate an observation.
    We can come back later and make this depend on Pac-Man's true location.
    Update: now there's a true Pac-Man object in the program.
    """
    return pacman.pos  # now the ghost believes based on Pac-Man's real location


def transition_model(pos):
    """
    Return valid neihboring position from which Pac-Man could have moved.
    """
    return maze.neighbors(pos)


def emission_model(pos, obs):
    """
    Now we define how lokely we are to observe evidence if Pac-Man is at position 'pos.'
    Current setup: inverse function of Manhattan distance from the observed position.
    """
    x1, y1 = pos
    x2, y2 = obs
    dist = abs(x1 - x2) + abs(y1 - y2)
    return 1.0 / (1 + dist)  # the value should decrease with distance


# main game loop
while True:
    # handle quit event (e.g., close window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman.move((0, -1), maze)
            elif event.key == pygame.K_DOWN:
                pacman.move((0, 1), maze)
            elif event.key == pygame.K_LEFT:
                pacman.move((-1, 0), maze)
            elif event.key == pygame.K_RIGHT:
                pacman.move((1, 0), maze)
    # now we need to set up the HMM and ghost movement

    # step 1: receive (simulated) observation of Pac-Man

    obs = fake_observation()

    # step 2: update belief state with forward algorithm
    belief.update(obs, transition_model, emission_model)

    # step 3: ghost decides where to go based on belief + A* pathfinding
    ghost.update(belief, maze)

    # finally we draw everything
    screen.fill((0, 0, 0))  # clear screen (black background)
    draw_grid(screen, maze, belief, ghost, pacman)
    pygame.display.flip()  # refresh the window
    clock.tick(FPS)  # wait to maintain desired FPS
