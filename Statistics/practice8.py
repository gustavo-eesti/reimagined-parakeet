"""Creating a probability distribution
A new restaurant opened a few months ago, and the restaurant's management wants to optimize its
seating space based on the size of the groups that come most often. On one night, there are
10 groups of people waiting to be seated at the restaurant, but instead of being called in the order they arrived,
they will be called randomly. In this exercise, you'll investigate the probability of groups of
different sizes getting picked first. Data on each of the ten groups is contained in the
restaurant_groups DataFrame."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# initialize list of lists
data = [['A', 2], ['B', 4], ['C', 6], ['D', 2], ['E', 2],
        ['F', 2], ['G', 3], ['H', 2], ['I', 4], ['J', 2]]

# Create the pandas DataFrame
restaurant_groups = pd.DataFrame(data, columns=['group_id', 'group_size'])

# Create a histogram of restaurant_groups and show plot
restaurant_groups['group_size'].hist(bins=[2, 3, 4, 5, 6])
plt.show()

# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]

# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

print(size_dist)

# Calculate expected value
expected_value = sum(size_dist['group_size'] * size_dist['prob'])
print(expected_value)

# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist['group_size'] >= 4]
print(groups_4_or_more)
# Sum the probabilities of groups_4_or_more
prob_4_or_more = sum(groups_4_or_more['prob'])
print(prob_4_or_more)
