# Import numpy with alias np
import numpy as np
import pandas as pd

food_consumption = pd.read_csv('.././datasets/food_consumption.csv', index_col=0)

# Filter for Belgium
be_consumption = food_consumption[food_consumption['country'] == 'Belgium']

# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# Calculate mean and median consumption in Belgium
print(be_consumption['consumption'].agg('mean'))
print(be_consumption['consumption'].agg('median'))

# Calculate mean and median consumption in USA
print(usa_consumption['consumption'].agg('mean'))
print(usa_consumption['consumption'].agg('median'))

# Subset for Belgium and USA only
be_and_usa = food_consumption[(food_consumption['country'] == 'Belgium') |
                              (food_consumption['country'] == 'USA')]

# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby('country')['consumption'].agg(['mean', 'median']))
