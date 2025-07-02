# main.py
# this file contains the game's simulation loop

from grid import MazeGrid
from ghost import Ghost
from belief import BeliefState

# set up a 10x10 grid with some walls
maze = MazeGrid(width=10, height=10, walls=[(5, 5), (5, 6), (5, 7)])
# place ghost at (0, 0)
ghost = Ghost(start_pos=(0, 0))
# set up initial uniform belief
belief = BeliefState(width=10, height=10)


def fake_observation():
    """
    Fake observations might be useful for testing purposes.
    Here we simulate an observation.
    We can come back later and make this depend on Pac-Man's true location.
    """
    return (8, 8)


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


# now we can run the simulation
# starting with 20 time steps
for t in range(20):
    obs = fake_observation()  # simulated sensor input
    belief.update(obs, transition_model, emission_model)
    ghost.update(belief, maze)

    print(f"Time: {t}")
    print(f"Ghost is at: {ghost.pos}")
    print(f"Most likely Pac-Man location: {belief.most_likely_position()}")
