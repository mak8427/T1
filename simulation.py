import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functions import *
def Simulation():
    # Set mean and standard deviation
    mu, sigma = 400, 200

    # Generate random data from a left-skewed distribution using numpy
    data = np.random.gamma(6, 100, 1000000)
    data = (data - np.mean(data)) / np.std(data)
    data = (data * sigma) + mu

    # Plot the histogram of the generated data
    #plt.hist(data, bins=100, density=True, alpha=0.6, color='g')
    #plt.show()

    #create 3 protucts with random values
    product_list=[Product(id=0),Product(id=1),Product(id=2)]
    agent_list=[consumer(data) for i in range(100000)]
    for x in range(10):
        s1=time.time()

        buy_product_multiprocessed(agent_list,product_list)

        compute_profit(product_list)
        s2=time.time()-s1
        t1=time.time()
        for product in product_list:
            product.new_product()
        t2=time.time()-t1

        print("proportion of time spent in buy_product: ", s2/t2)
    for product in product_list:
        print(np.sum(product.profit_history))
    return product_list,agent_list
if "__main__" == __name__:
    r=Simulation()
    print("fine")