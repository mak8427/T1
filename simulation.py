import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functions import *
import pandas as pd
from RL import *

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
def Simulation():
    # Set mean and standard deviation
    mu, sigma = 450, 200
    # Generate random data from a left-skewed distribution using numpy
    data = np.random.gamma(6, 100, 100000)
    data = (data - np.mean(data)) / np.std(data)
    data = (data * sigma) + mu

    # Plot the histogram of the generated data
    plt.hist(data, bins=100, density=True, alpha=0.6, color='g')
    plt.show()

    #create 3 protucts with random values
    product_list=[Product(id=0),Product(id=1),Product(id=2)]
    agent_list=[consumer(data) for i in range(1500)]


    #create the q table
    state_size, ranges=get_state_space(agent_list, product_list,data)

    action_size= 3
    q_table = np.random.uniform(low=-2, high=0, size=(state_size + [10]))

    df = pd.DataFrame(columns=["stato0","stato1","profit1","profit2","profit3","price_chosen"])


    discrete_os_size = get_state_space(agent_list, product_list,data)
    print(discrete_os_size)
    discrete_os_win_size = (max(data)-min(data)) / discrete_os_size[0]
    LEARNING_RATE=0.95

    s1 = time.time()





    for x in range(10000):
        #get current state
        state=get_state(product_list,ranges,with_agent=True)
        #print("state:",state)
        stato=q_table[state[0]][state[1]]
        #print("best", np.argmax(stato))

        #compute the action
        product_list[-1]=Product(id=2,cost_to_produce=ranges[np.argmax(stato)],agent=True)

        #compute profit and trade
        buy_product(agent_list, product_list)
        compute_profit(product_list)

        #compute reward
        reward=compute_reward(product_list)

        q_table[state[0]][state[1]][np.argmax(stato)] += LEARNING_RATE * (reward - q_table[state[0]][state[1]][np.argmax(stato)])

        #print("selling price 1: ", product_list[0].selling_price, "   selling price 2: ", product_list[1].selling_price)

        df=df.append({"stato0":state[0],"stato1":state[1],
                      "profit1":product_list[0].profit_history[-1],"profit2":product_list[1].profit_history[-1],"profit3":product_list[2].profit_history[-1],
                      "price_chosen1":product_list[0].selling_price,"price_chosen2":product_list[1].selling_price,"price_chosen3":product_list[2].selling_price,
                      "unit_sold1":product_list[0].number_sold,"unit_sold2":product_list[1].number_sold,"unit_sold3":product_list[2].number_sold }, ignore_index=True)


        for product in product_list:
            if product.seller_id!=2:
                product.new_product()

        if x%100==0:
            print("iteration: ", x)

        #print("proportion of time spent in buy_product: ", s2)
    for product in product_list:
        print(np.sum(product.profit_history))

    df.to_csv('data.csv', index=False, encoding='utf-8')

    s2 = time.time() - s1
    print("time to execute ", s2)


    return product_list,agent_list


if "__main__" == __name__:
    r=Simulation()
    print("fine")