import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functions import *
from RL import *
def Simulation():
    # Set mean and standard deviation
    mu, sigma = 450, 200
    # Generate random data from a left-skewed distribution using numpy
    data = np.random.gamma(6, 100, 1000000)
    data = (data - np.mean(data)) / np.std(data)
    data = (data * sigma) + mu

    # Plot the histogram of the generated data
    plt.hist(data, bins=100, density=True, alpha=0.6, color='g')
    plt.show()

    #create 3 protucts with random values
    product_list=[Product(id=0),Product(id=1),Product(id=2)]
    agent_list=[consumer(data) for i in range(10000)]


    #create the q table
    state_size, ranges=get_state_space(agent_list, product_list,data)

    action_size= 3
    q_table = np.random.uniform(low=-2, high=0, size=(state_size + [10]))


    discrete_os_size = get_state_space(agent_list, product_list,data)
    print(discrete_os_size)
    discrete_os_win_size = (max(data)-min(data)) / discrete_os_size[0]



    for x in range(2):
        s1=time.time()



        buy_product(agent_list, product_list)
        compute_profit(product_list)
        s2=time.time()-s1
        print("state:",get_state(product_list,ranges,with_agent=True))



        for product in product_list:
            if product.seller_id!=3:
                product.new_product()

        print("proportion of time spent in buy_product: ", s2)
    for product in product_list:
        print(np.sum(product.profit_history))
    return product_list,agent_list
if "__main__" == __name__:
    r=Simulation()
    print("fine")