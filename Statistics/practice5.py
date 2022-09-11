"""Finding outliers using IQR
Outliers can have big effects on statistics like mean, as well as statistics that rely on the mean,
such as variance and standard deviation. Interquartile range, or IQR, is another way of measuring spread
that's less influenced by outliers. IQR is also often used to find outliers.
If a value is less than Q1 − 1.5 × IQR or greater than Q3 + 1.5 × IQR,
it's considered an outlier. In fact, this is how the lengths of the whiskers
in a matplotlib box plot are calculated."""
import pandas as pd
import numpy as np

food_consumption = pd.read_csv('.././datasets/food_consumption.csv', index_col=0)

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission']\
    .agg('sum')   # .sum() would also work instead of .agg('sum')

statistics_country = food_consumption[food_consumption['country'] == 'Estonia']\
    .agg('describe')    # out of the scope of the exercise. just practicing
print(emissions_by_country)
print(statistics_country)

# Compute the first and third quartiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
q2 = np.quantile(emissions_by_country, 0.5)  # median
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country > upper) |
                                (emissions_by_country < lower)]
print(outliers)
