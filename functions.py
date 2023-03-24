import secrets
import math
import traceback
import numpy as np
import matplotlib.pyplot as plt
import time

class Product:
    def __init__(self,selling_markup=secrets.choice(range(300)),cost_to_produce=secrets.choice(range(1000)),number_produced=secrets.choice(range(5000))+2000,id=0):
        self.cost_to_produce = secrets.choice(range(150,300))
        self.selling_price = secrets.choice(range(50,100))+self.cost_to_produce
        self.number_produced=secrets.choice(range(2000,5000))+200
        self.number_sold=0
        self.seller_id=id
        self.quality_factor = self._calculate_quality_factor()
        self.profit_history = []


    def calculate_profit(self):
        profit=self.selling_price * self.number_sold - self.cost_to_produce * self.number_produced
        self.profit_history.append(profit)
        return profit

    def _calculate_quality_factor(self, w1=0.1, w0=-4.6):
        w_x = w0 + w1 * self.selling_price / 10
        return (10 / (1 + math.exp(-w_x))) + math.log10(self.selling_price)

    def new_product(self):

        self.cost_to_produce = secrets.choice(range(150,300))
        self.selling_price = secrets.choice(range(50,100))+self.cost_to_produce
        self.number_produced=secrets.choice(range(2000,5000))+200
        self.number_sold=0
        self.quality_factor = self._calculate_quality_factor()

    def __str__(self):
        return "Product: selling_price: {}, cost_to_produce: {}, number_produced: {}, number_sold: {}, seller_id: {}, quality_factor: {}".format(
            self.selling_price, self.cost_to_produce, self.number_produced, self.number_sold, self.seller_id, self.quality_factor
        )

class consumer:
    def __init__(self,data):

        #random distribution with sigma 2 mean 200
        self.capital =  secrets.choice(data)
        self.agent_10y_history=[]
        self.agent_preference_seller={0:0,1:0,2:0}


    def product_score(self,product):
        if product.selling_price>self.capital:
            return 0
        return (product.quality_factor/product.selling_price * 50.55555)*(0.7+self.agent_preference_seller[product.seller_id]*0.2+secrets.choice(range(10))*0.01)

    def capital_change(self,data):
        self.capital = secrets.choice(data)

    def update_agent_preference(self):
        for i in range(3):
            self.agent_preference_seller[i]=self.agent_10y_history.count(i)/10





import concurrent.futures

def buy_product_for_agent(agent, product_list):
    try:
        best = 0
        best_product = None
        for product in product_list:
            if agent.capital > product.selling_price and product.number_sold < product.number_produced:
                tmp = agent.product_score(product)
                if tmp > best:
                    best = tmp
                    best_product = product.seller_id

        if best != 0 and best_product is not None:
            product_list[best_product].number_sold += 1
            agent.agent_10y_history.append(best_product)
            if len(agent.agent_10y_history) > 10:
                agent.agent_10y_history.pop(0)
            agent.update_agent_preference()
            return 0
        else:
            return 1
    except Exception as e:
        print(f"Error in buy_product_for_agent for agent {agent}: {e}")
        print(traceback.format_exc())
        return -1
import itertools


def buy_product_multiprocessed(agent_list, product_list, batch_size=100):
    out_of_market = 0
    for agent in agent_list:
        out_of_market += buy_product_for_agent(agent, product_list)





    print("Agents out of the market :", out_of_market)





def compute_profit(product_list):
    for product in product_list:
        print("profit of product ",product.seller_id," is ",product.calculate_profit())

# Function to create a list of dictionaries from agent_list
def create_agent_data(agent_list):
    agent_data = []
    for agent in agent_list:
        agent_data.append({
            'capital': agent.capital,
            'agent_10y_history': agent.agent_10y_history,
            'agent_preference_seller': agent.agent_preference_seller
        })
    return agent_data



# Function to create a list of dictionaries from product_list
def create_product_data(product_list):
    product_data = []
    for product in product_list:
        product_data.append({
            'cost_to_produce': product.cost_to_produce,
            'selling_price': product.selling_price,
            'number_produced': product.number_produced,
            'number_sold': product.number_sold,
            'seller_id': product.seller_id,
            'quality_factor': product.quality_factor
        })
    return product_data