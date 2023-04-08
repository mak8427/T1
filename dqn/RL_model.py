import numpy as np
import random
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from collections import deque
from  functions import *

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95  # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay


class MarketEnvironment:
    def __init__(self, data, agent_list, product_list):
        self.data = data
        self.agent_list = agent_list
        self.product_list = product_list

    def reset(self):
        self.product_list = [Product(id=i) for i in range(3)]

    def step(self, action, product_id):
        # Apply action
        if action == 0:
            self.product_list[product_id].cost_to_produce *= 0.95
        elif action == 1:
            self.product_list[product_id].cost_to_produce *= 1.05
        elif action == 2:
            self.product_list[product_id].selling_price *= 0.95
        elif action == 3:
            self.product_list[product_id].selling_price *= 1.05

        buy_product(self.agent_list, self.product_list)
        compute_profit(self.product_list)

        reward = self.compute_ranking(product_id)

        self.product_list[product_id].new_product()

        return np.array([self.product_list[product_id].cost_to_produce, self.product_list[product_id].selling_price]), reward, False

    def compute_ranking(self, product_id):
        profit_list = [product.calculate_profit() for product in self.product_list]
        ranking = sorted(range(len(profit_list)), key=lambda k: profit_list[k], reverse=True)

        # Get the index of the product_id in the ranking list
        rank = ranking.index(product_id)



        # Calculate the reward based on the ranking
        if rank == 0:
            reward = 1
        elif rank == 1:
            reward = 0
        else:
            reward = -1

        return reward
