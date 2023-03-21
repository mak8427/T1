import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time

class Product:
    def __init__(self,selling_markup=random.randint(0,300),cost_to_produce=random.randint(1,1000),number_produced=random.randint(2000,7000)):
        self.cost_to_produce = cost_to_produce
        self.quality_factor = self._calculate_quality_factor()
        self.selling_price = selling_markup+cost_to_produce
        self.number_produced=number_produced
        self.number_sold=0

    def calculate_profit(self):
        return self.selling_price * self.number_sold - self.cost_to_produce * self.number_produced

    def _calculate_quality_factor(self, w1=0.1, w0=-5.2):
        w_x = w0 + w1 * self.cost_to_produce
        return (1 / (1 + math.exp(-w_x)) * 10 )+ math.log(self.cost_to_produce)

class consumer:
    def __init__(self,data):

        random.seed(time.time())
        #random distribution with sigma 2 mean 200
        self.capital = random.choice(data)
        self.agent_history=[]
        self.agent_preference_seller1=0
        self.agent_preference_seller2=0

    def product_score(self,product):
        score=0
        if product.selling_price>self.capital:
            return score
        score=score+product.quality_factor/product.selling_price *65




def buy_product(agent_list,product_list):
    product_list.sort(key=lambda x: x.selling_price)


