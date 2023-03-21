import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functions import *

# Set mean and standard deviation
mu, sigma = 600, 200

# Generate random data from a left-skewed distribution using numpy
data = np.random.gamma(6, 100, 1000000)
data = (data - np.mean(data)) / np.std(data)
data = (data * sigma) + mu

# Plot the histogram of the generated data
#plt.hist(data, bins=100, density=True, alpha=0.6, color='g')
#plt.show()

#create 3 protucts with random values
product_list=[Product(id=0),Product(id=1),Product(id=2)]
agent_list=[consumer(data) for i in range(10000)]
buy_product(agent_list,product_list)
compute_profit(product_list)

print("fine")