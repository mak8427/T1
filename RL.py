import numpy as np
import random
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from collections import deque
from  functions import *


def get_state_space(agent_list, product_list,data):
    ranges=[]
    data.sort()
    #make 10 ranges of data values
    for i in range(10):
        ranges.append(data[int(len(data)/10*i)])
    ranges.append(data[-1])
    print(ranges)
    dim_space= [len(ranges), len(ranges)]
    return dim_space,ranges











class agent:
    def __init__(self, id, data):
        self.profit_history = []
        self.id = id
        self.data = data

