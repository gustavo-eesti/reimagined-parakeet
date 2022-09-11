import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

food_consumption = pd.read_csv('.././datasets/food_consumption.csv', index_col=0)

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Histogram of co2_emission for rice and show plot
plt.hist(rice_consumption['co2_emission'])
plt.show()

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption['co2_emission'].agg(['mean', 'median']))
