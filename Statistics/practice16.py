"""Simulating sales under new market condition
The company's financial analyst is predicting that next quarter, the worth of each sale will increase
by 20% and the volatility, or standard deviation, of each sale's worth will increase by 30%.
To see what Amir's sales might look like next quarter under these new market conditions,
you'll simulate new sales amounts using the normal distribution and store these in the new_sales DataFrame,
which has already been created for you.

norm.rvs = normal distribution / random variates
"""
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

amir_deals = pd.read_csv('.././datasets/amir_deals.csv', index_col=0)
mean_deals = np.mean(amir_deals['amount'])
std_deals = np.std(amir_deals['amount'])

# Calculate new average amount
new_mean = mean_deals * 1.2

# Calculate new standard deviation
new_sd = std_deals * 1.3

# Simulate 36 new sales
new_sales = norm.rvs(new_mean, new_sd, size=36)

# Create histogram and show
plt.hist(new_sales)
plt.show()
