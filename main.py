import  numpy as np
import matplotlib.pyplot as plt
def main():
    #build a neural network from scratch
    #define the input data as a sin function of shape (1,100) with 70% missing values from 0 to 2
    x = np.sin(np.linspace(0,2*np.pi,100)).reshape(1,100)
    x = np.where(np.random.rand(1,100) < 0.1, x, np.nan)
    #plot the input data
    plt.scatter(list(range(0,len(x[0]))),x[0])
    plt.show()
    #activation function
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    #the architecture of the neural network will be the following:
    #input layer: 1 neuron
    #3 hidden layers: 10 neurons each
    #output layer: 1 neuron
    #the weights and biases will be initialized randomly
    #the weights and biases will be updated using gradient descent

    class Layer_Dense:
        def __init__(self, n_inputs, n_neurons): #initialize the weights and biases
            self.weights = 0.1 * np.random.randn(n_inputs, n_neurons) #initialize the weights to random values
            self.biases = np.zeros((1, n_neurons)) #initialize the biases to 0
        def forward(self, inputs):#forward propagation (calculate the output of the layer)
            self.output = np.dot(inputs, self.weights) + self.biases #calculate the output of the layer
        def backward(self, dvalues):#backward propagation (calculate the gradients)
            self.dweights = np.dot(self.inputs.T, dvalues) #
            self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
            self.dinputs = np.dot(dvalues, self.weights.T)













    return


if __name__ == '__main__':
    main()
#
