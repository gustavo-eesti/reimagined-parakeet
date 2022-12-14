"""Data back-ups
The sales software used at your company is set to automatically back itself up, but no one knows exactly
what time the back-ups happen. It is known, however, that back-ups happen exactly every 30 minutes.
Amir comes back from sales meetings at random times to update the data on the client he just met with.
He wants to know how long he'll have to wait for his newly-entered data to get backed up. Use your
new knowledge of continuous uniform distributions to model this situation and answer Amir's questions."""

import pandas as pd
import numpy as np
from scipy.stats import uniform

amir_deals = pd.read_csv('.././datasets/amir_deals.csv', index_col=0)

# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Calculate probability of waiting less than 5 mins
prob_less_than_5 = uniform.cdf(5, min_time, max_time)
prob_greater_than_5 = 1 - prob_less_than_5
print(prob_less_than_5)
print(prob_greater_than_5)

# Calculate probability of waiting 10-20 mins
prob_between_10_and_20 = uniform.cdf(20, min_time, max_time) - uniform.cdf(10, min_time, max_time)
print(prob_between_10_and_20)