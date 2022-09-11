""" Quartiles, quantiles, and quintiles
Quantiles are a great way of summarizing numerical data since they can be used to measure center and spread,
as well as to get a sense of where a data point stands in relation to the rest of the data set.
For example, you might want to give a discount to the 10% most active users on a website.
In this exercise, you'll calculate quartiles, quintiles, and deciles, which split up a dataset
into 4, 5, and 10 pieces, respectively."""

import pandas as pd
import numpy as np

food_consumption = pd.read_csv('.././datasets/food_consumption.csv', index_col=0)

a = np.quantile(food_consumption['co2_emission'], 0.5)  # returns the mean
quartiles_co2 = np.quantile(food_consumption['co2_emission'], [0, 0.25, 0.5, 0.75, 1])  # returns the quartiles
quintiles_co2 = np.quantile(food_consumption['co2_emission'], [0, 0.2, 0.4, 0.6, 0.8, 1])   # returns the quintiles
deciles_co2 = np.quantile(food_consumption['co2_emission'], [0, 0.1, 0.2, 0.3, 0.4, 0.5,
                                                             0.6, 0.7, 0.8, 0.9, 1])    # returns the deciles
deciles_co2_better = np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 11))

# Calculate the quartiles of co2_emission
print(quartiles_co2)

# Calculate the quintiles of co2_emission
print(quintiles_co2)

# Calculate the deciles of co2_emission
print(deciles_co2)
print(deciles_co2_better)
