import sys
sys.path.insert(0, '/Users/prathamgandhi/Desktop/Personal/constellation/Constellation/modules')
from NeuralNetwork import NeuralNetwork

import numpy as np

X = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])
y = np.array([[0],[1],[1],[0]])
nn = NeuralNetwork(X,y)

for i in range(100000):
    nn.feedforward()
    nn.backprop()

print(nn.output)