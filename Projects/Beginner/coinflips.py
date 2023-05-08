# This program simulates a coin flipping experiment and calculates the experimental probability of getting two heads in a row when flipping two coins.
# It does this by flipping two coins at random and checking if both coins come up heads.
# It repeats this experiment a large number of times (specified by num_trials)
# and keeps track of the proportion of times both coins came up heads up to that point.
# Finally, it plots the experimental probability of getting two heads in a row
# against the number of flips and compares it to the theoretical probability (0.25, or 1/4).

import matplotlib.pyplot as plt
import numpy as np


def coin_flip_experiment():
    # defining our two coins as lists
    coin1 = ["Heads", "Tails"]
    coin2 = ["Heads", "Tails"]

    # "flipping" both coins randomly
    coin1_result = np.random.choice(coin1)
    coin2_result = np.random.choice(coin2)

    # checking if both flips are heads
    if coin1_result == "Heads" and coin2_result == "Heads":
        return 1
    else:
        return 0


# how many times we run the experiment
num_trials = 100000
prop = []
flips = []
# keep track of the number of times heads pops up twice
two_heads_counter = 0

# perform the experiment five times
for flip in range(num_trials):
    # if both coins are heads add 1 to the counter
    two_heads_counter += coin_flip_experiment()
    # keep track of the proportion of two heads at each flip
    prop.append(two_heads_counter / (flip + 1))
    # keep a list for number of flips
    flips.append(flip + 1)

# plot all flips and proportion of two heads
plt.plot(flips, prop, label="Experimental Probability")
plt.xlabel("Number of Flips")
plt.ylabel("Proportion of Two Heads")

plt.hlines(0.25, 0, num_trials, colors="orange", label="True Probability")
plt.legend()


plt.show()
