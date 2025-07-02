# belief.py
# this file contains the logic for the Forward Algorithm

# imports
import numpy as np


class BeliefState:
    def __init__(self, width, height):
        """
        Initialize a uniform belief over all cells.
        """
        self.width = width
        self.height = height
        self.belief = np.full(
            (width, height), 1.0 / (width * height)
        )  # uniform prior distribution

    def normalize(self):
        """
        We need to normalize belief so all probabilities sum to 1.
        """
        total = np.sum(self.belief)
        if total > 0:
            self.belief = self.belief / total

    def update(self, observation, transition_model, emission_model):
        """
        Here is where we actually start performing the Forward Algorithm.
        For each state x_t, sum over all possible x_t(t-1) using
        transition probabilities and emission probabilities.
        """
        new_belief = np.zeros((self.width, self.height))

        for x in range(self.width):
            for y in range(self.height):
                prob = 0.0
                # sum over all predecessors that could transition to (x, y)
                for dx, dy in transition_model((x, y)):
                    prob += self.belief[dx, dy] / len(transition_model((dx, dy)))
                # now multiply by likelihood of observing current evidence at (x, y)
                new_belief[x, y] = prob * emission_model((x, y), observation)

        self.belief = new_belief
        self.normalize()

    def most_likely_position(self):
        """
        Return the position with the highest belief, i.e.,
        the position Pac-Man is most likely to be.
        """
        return np.unravel_index(np.argmax(self.belief), self.belief.shape)
