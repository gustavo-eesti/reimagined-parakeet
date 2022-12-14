"""Simulating sales deals
Assume that Amir usually works on 3 deals per week, and overall, he wins 30% of deals he works on.
Each deal has a binary outcome: it's either lost, or won, so you can model his sales deals with a binomial
distribution. In this exercise, you'll help Amir simulate a year's worth of his deals, so he can better
understand his performance.

binom.rvs = binomial random variates"""
import numpy as np
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate a single deal
print(binom.rvs(1, 0.3, size=1))

# Simulate 1 week of 3 deals
np.random.seed(10)
print(binom.rvs(3, 0.3, size=1))

# Simulate 52 weeks of 3 deals
np.random.seed(10)

deals = binom.rvs(3, 0.3, size=52)

# Print mean deals won per week
print(np.mean(deals))
