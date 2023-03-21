import secrets
import math
import numpy as np
import matplotlib.pyplot as plt
import time

class Product:
    def __init__(self,selling_markup=secrets.choice(range(300)),cost_to_produce=secrets.choice(range(1000)),number_produced=secrets.choice(range(5000))+2000,id=0):
        self.cost_to_produce = secrets.choice(range(150,1000))
        self.selling_price = secrets.choice(range(50,300))+cost_to_produce
        self.number_produced=secrets.choice(range(2000,5000))+200
        self.number_sold=0
        self.seller_id=id
        self.quality_factor = self._calculate_quality_factor()


    def calculate_profit(self):
        return self.selling_price * self.number_sold - self.cost_to_produce * self.number_produced

    def _calculate_quality_factor(self, w1=0.1, w0=-4.6):
        w_x = w0 + w1 * self.selling_price / 10
        return (10 / (1 + math.exp(-w_x))) + math.log10(self.selling_price)

class consumer:
    def __init__(self,data):

        #random distribution with sigma 2 mean 200
        self.capital =  secrets.choice(data)
        self.agent_10y_history=[]
        self.agent_preference_seller={0:0,1:0,2:0}


    def product_score(self,product):
        score=0
        if product.selling_price>self.capital:
            return score
        score=score+product.quality_factor/product.selling_price * 50.55555
        score=score*(0.7+self.agent_preference_seller[product.seller_id]*0.2+secrets.choice(range(10))*0.01)
        return score

    def capital_change(self,data):
        self.capital = secrets.choice(data)

    def update_agent_preference(self):
        for i in range(3):
            self.agent_preference_seller[i]=self.agent_10y_history.count(i)/10





def buy_product(agent_list,product_list):
    product_list.sort(key=lambda x: x.selling_price)
    for agent in agent_list:
        best=0
        for product in product_list:
            if agent.capital>product.selling_price:
                tmp=agent.product_score(product)
                if tmp > best:
                    best=tmp
                    best_product=product.seller_id

        product_list[best_product].number_sold+=1

        if len (agent.agent_10y_history)<10:
            agent.agent_10y_history.append(best_product)
        if len(agent.agent_10y_history)<=10:
            agent.agent_10y_history.pop(0)
            agent.agent_10y_history.append(best_product)
        agent.update_agent_preference()

def compute_profit(product_list):
    for product in product_list:
        print("profit of product ",product.seller_id," is ",product.calculate_profit())




