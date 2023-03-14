import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf

# Generate data
X = np.arange(0, 2*np.pi, 0.1)  # input values
y = np.sin(X)  # target values


# Split data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=42)

# Print the shape of the resulting arrays
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)




# Define the model
model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=10, verbose=0)

# Evaluate the model on the test set
mse = model.evaluate(X_test, y_test, verbose=0)
print("Mean Squared Error: {:.4f}".format(mse))

y_pred = model.predict(X_test)

# Plot the actual and predicted values
plt.scatter(X_test, y_test, label='Actual')
plt.scatter(X_test, y_pred, label='Predicted')
plt.legend()
plt.show()