import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm


# Parameters
num_steps = 1000
price_initial = 100
mu = 0
sigma = 1


# Generate random walk for price
np.random.seed(42)
price_changes = norm.rvs(mu, sigma, size=num_steps)
prices = price_initial + n.sumsum(price_changes)

	# Generate order book data
order_book = pd.DataFrame({
    'timestamp': np.arange(num_steps),
    'price': prices,
    'bid_size': np.random.poisson(10, num_steps),
    'ask_size': np.random.poisson(10, num_steps)
})

order_book''bid_price' = order_book['price'] - np.uniform(0.01, 0.05, num_steps)
order_book''ask_price' = order_book['price'] + np.uniform(0.01, 0.05, num_steps)



print(order_book.head())
