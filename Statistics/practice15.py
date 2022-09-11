"""Probabilities from the normal distribution
Since each deal Amir worked on (both won and lost) was different, each was worth a different amount of money.
These values are stored in the amount column of amir_deals and follow a normal distribution with a mean of
5000 dollars and a standard deviation of 2000 dollars. As part of his performance metrics,
you want to calculate the probability of Amir closing a deal worth various amounts.

norm.cdf = normal distribution / cumulative distribution function.
norm.ppf = normal distribution / percent point function (inverse of cdf — percentiles)."""

from scipy.stats import norm
import pandas as pd
import numpy as np

amir_deals = pd.read_csv('.././datasets/amir_deals.csv', index_col=0)

mean_deals = np.mean(amir_deals['amount'])
std_deals = np.std(amir_deals['amount'])

# Probability of deal < 7500
prob_less_7500 = norm.cdf(7500, mean_deals, std_deals)

print(prob_less_7500)

# Probability of deal > 1000
prob_over_1000 = 1 - norm.cdf(1000, mean_deals, std_deals)

print(prob_over_1000)

# Probability of deal between 3000 and 7000
prob_3000_to_7000 = norm.cdf(7000, mean_deals, std_deals) - norm.cdf(3000, mean_deals, std_deals)

print(prob_3000_to_7000)

# Calculate amount that 25% of deals will be less than
pct_25 = norm.ppf(0.25, mean_deals, std_deals)

print(pct_25)
