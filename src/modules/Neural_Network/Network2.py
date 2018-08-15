import random 
import sys
sys.path.insert(0, '../src/modules/Arithmetic_Toolkit')
from Linear_Algebra import Vectors
import math

def sigmoid(t):
	return 1/(1+math.exp(-t))

def neuron_output(weights,inputs):
	v = Vectors()
	return sigmoid(v.dot(weights,inputs))

def feed_forward(neural_network, input_vector):
	"""takes in a neural entwork
	(represented as a list of lists of lists of weights)
	and returns the output from forward-propogating the input"""

	outputs = []

	# process one layer at a time
	for layer in neural_network:
		input_with_bias = input_vector + [1]				# add a bias input
		output = [neuron_output(neuron, input_with_bias)	# compute the output
					for neuron in layer]					# for each neuron
		outputs.append(output)								# and remember it

		# then the input to the next layer is the output of this one
		input_vector = output

	return outputs

def backpropagate(network, input_vector, targets):
	hidden_outputs, outputs = feed_forward(network, input_vector)

	# the output * (1-ouput) is from the derivate of sigmoid
	output_deltas = [output * (1-output) * (output-target) 
					for output, target, in zip(outputs, targets)]

	# the output * (1-output) is from the derivate of sigmoid
	for i, output_neuron in enumerate(network[-1]):
		# focus on the ith output layer neuron
		for j, hidden_output in enumerate(hidden_outputs + [1]):
			# adjust the jth weight based on both
			# this neuron's delta and its jth input
			output_neuron[j] -= output_deltas[i] * hidden_output

	# back-propagate errors to hidden layer
	v = Vectors()
	hidden_deltas = [hidden_output * (1-hidden_output) *
					v.dot(output_deltas, [n[i] for n in network[-1]])
					for i, hidden_output in enumerate(hidden_outputs)]

	# adjust weights for hidden layer, one neuron at a time
	for i, hidden_neuron in enumerate(network[0]):
		for j, input in enumerate(input_vector + [i]):
			hidden_neuron[j] -= hidden_deltas[i] * input

def predict(input, network):
	return feed_forward(network, input)[-1]

def main():
	print("not implemented")

if __name__ == "__main__":
	main()