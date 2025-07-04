# belief.py
# this file contains the logic for the Forward Algorithm

# imports
import numpy as np


class BeliefState:
    def __init__(self, width, height):
        """
        Initialize a uniform belief over all cells.
        This algorithm will compute a probability distribution over hidden states at each
            time step after being given a sequence of observations.
        In the Pac-Man game...
            1. Hidden state is Pac-Man's actual position (which the ghost cannot directly see)
            2. Observation: noisy evidence (e.g., pellet eaten, sound)
            3. Forward Algorithm let's the ghost infer where pac-man might be and make
                updates to its belief system
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

        For how the algorithm unfolds...
            1. start with a uniform belief distribution
            2. receive an observation
            3. for each tile...
                look at which tiles pac-man could have come from
                use transmission probabilities to weigh how likely he was to have
                    come from that tile
                use emission probabilities to update based on current evidence

        transition probability = "Where did Pac-Man make that noise from?"
        emission probability = "Where is Pac-Man now?"
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
