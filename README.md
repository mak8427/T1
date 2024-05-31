# Simulation of Neural Networks and Reinforcement Learning Applications in Economics

## Overview
This project explores the application of neural networks and reinforcement learning (RL) in an economic simulation involving competitive pricing strategies among sellers. The primary focus is to develop and analyze a Q-learning algorithm that optimizes the pricing strategy to maximize the profit of selling agents in a simulated marketplace.

## Contents
1. [Introduction](#introduction)
2. [Simulation Setup](#simulation-setup)
3. [Neural Networks and Q-learning Implementation](#neural-networks-and-q-learning-implementation)
4. [Usage](#usage)
5. [Dependencies](#dependencies)
6. [Running the Simulation](#running-the-simulation)
7. [Visualization and Results](#visualization-and-results)
8. [Further Reading](#further-reading)

## Introduction
The idea of artificial neural networks as electronic brains dates back to 1943 when Warren McCulloch and Walter Pitts created an electronic circuit to simulate the functioning of neurons and their connections. This project builds on these foundational concepts to simulate a marketplace where agents interact using neural networks and reinforcement learning algorithms.

## Simulation Setup
The marketplace simulation involves:
- **Sellers**: Each seller produces a product with specific costs and markups.
- **Buyers**: Buyers have budgets and select products based on utility, price, and seller preference.
- **Utility Calculation**: Utility is derived from the product's quality and price.
- **Profit Calculation**: Sellers calculate profit based on the number of products sold and the cost of production.

## Neural Networks and Q-learning Implementation
### Neural Networks
A simple neural network is designed to predict the best selling price based on historical data:
- **Input Layer**: Represents product features.
- **Hidden Layers**: Three layers with 10 neurons each, using ReLU activation functions.
- **Output Layer**: Produces the predicted selling price.

### Q-learning
Q-learning is used to optimize the pricing strategy:
- **Q-table**: Stores the Q-values for each state-action pair.
- **States**: Represent different pricing strategies.
- **Actions**: Represent possible adjustments to the selling price.
- **Reward**: Based on the profit made by the seller.

## Usage
### Initialization
1. **Initialize Sellers and Buyers**: Sellers are initialized with random production costs and markups, while buyers are initialized with a budget distribution.
2. **Run Simulation**: The simulation iterates through multiple cycles of buying and selling, updating Q-values based on rewards received.

### Functions
- **calculate_profit**: Calculates and stores the profit for each seller.
- **product_score**: Evaluates products based on utility and buyer preferences.
- **buy_product**: Facilitates the buying process for agents based on product scores.
- **new_product**: Resets product attributes for the next cycle.
- **Simulation**: Orchestrates the entire simulation process.

## Dependencies
- `numpy`
- `matplotlib`
- `pandas`
- `keras`
- `tensorflow`
- `concurrent.futures`
- `secrets`

## Running the Simulation
1. **Install Dependencies**: Ensure all the required libraries are installed.
   ```bash
   pip install numpy matplotlib pandas keras tensorflow
   ```
2. **Run the Simulation Script**: Execute the main simulation script.
   ```python
   if "__main__" == __name__:
       r = Simulation()
       print("Simulation Complete")
   ```

## Visualization and Results
The simulation produces various visualizations to analyze the performance of the agents:
- **Profit History**: Tracks the profit over time for each seller.
- **Product Scores**: Displays the utility scores for products.
- **Q-table Updates**: Shows the updates to the Q-values over iterations.

## Further Reading
For a deeper understanding of the concepts and methods used in this project, refer to the following sections of the accompanying thesis:
- **History and Functioning of Neural Networks**: Details the evolution of neural networks, including perceptrons, backpropagation, and activation functions.
- **Reinforcement Learning**: Explains the fundamentals of RL, including Q-learning and its application in economic simulations.
- **Application of Q-learning in Price Theory**: Describes how Q-learning is used to optimize pricing strategies in a competitive market.

## References
Refer to the bibliography section of the thesis for a comprehensive list of references used in this project.
