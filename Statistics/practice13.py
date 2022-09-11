"""How many sales will be won?
Now Amir wants to know how many deals he can expect to close each week if his win rate changes.
Luckily, you can use your binomial distribution knowledge to help him calculate the expected value in
different situations. Recall from the video that the expected value of a binomial distribution can
be calculated by n × p."""

import numpy as np
from scipy.stats import binom

# Expected number won with 30% win rate
won_30pct = 3 * 0.3
print(won_30pct)

# Expected number won with 25% win rate
won_25pct = 3 * 0.25
print(won_25pct)

# Expected number won with 35% win rate
won_35pct = 3 * 0.35
print(won_35pct)
