"""Distribution of Amir's sales
Since each deal Amir worked on (both won and lost) was different, each was worth a different amount of money.
These values are stored in the amount column of amir_deals As part of Amir's performance review,
you want to be able to estimate the probability of him selling different amounts, but before you can do this,
 you'll need to determine what kind of distribution the amount variable follows.
 """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

amir_deals = pd.read_csv('.././datasets/amir_deals.csv', index_col=0)

# Histogram of amount with 10 bins and show plot
amir_deals.hist('amount', bins=10)  # also works plt.hist(amir_deals['amount'], 10)
plt.show()
