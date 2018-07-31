from Input import Input

class Neuron:
	inputs = None
	bias = None

	def __input__(self, inputs, bias):
		"""Create new neuron with given inputs,
		a random initial bias (0.01-1), and
		a bias of bias
    	"""
		self.inputs = inputs
		self.bias = bias

	def getWeightedSumOfInputs():
		"""Return sum of every input
		multiplied by its weight
    	"""
		sum = 0.000
		for input in inputs:
			sum = sum+input.getWeightedValue()

	def getActivation:
		"""Return the weighted sum of inputs
		adjusted for bias
    	"""
		return self.getWeightedSumOfInputs()+bias

	def getOutput():
		"""Return the final output
		of the activation passed through
		the activation function, in this case
		sigmoid
    	"""
    	return sigmoid(getActivation())

    def sigmoid(activation):
    	"""Return the output of the
    	sigmoid activation fucntion
    	given an activation
    	"""
    	return 1.0/(1+ np.exp(-x))

   	def sigmoid_derivative(input):
   		"""Return the sigmoid derivative
   		for backprogatation
    	"""
   		return x * (1.0 - x)

	def setInputs(newInputs):
		"""Setter function used
		for adjusting the set of
		inputs
    	"""
		self.inputs = newInputs

	def setBias(newBias):
		"""Setter funciton used for
		changing the bias of a neuron
    	"""
		self.bias = newBias

	def getInputs():
		"""Return the list of
		inputs
    	"""
		return inputs

	def getBias():
		"""Return the bias of
		a neuron
    	"""
		return bias