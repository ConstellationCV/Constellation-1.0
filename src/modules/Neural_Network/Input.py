import numpy as np
class input:
	weight = None # holds the weight associated with this value (float)
	value = None # holds the value associated with this input (float)
	source = None # holds the source associated with this input edge (Neuron)
	sink = None # holds the sink associated with this input edge (Neuron)

	def __init__(self, value, source, sink):
		"""Create an input
		with value value and a
		random weight between 0.1-1"""
		self.weight = self.weight = np.random.random_sample()
		self.value = value
		self.source = source
		self.sink = sink

	def getWeight():
		"""Return the weight
		of this input"""
		return weight

	def getValue():
		"""Return the value
		of this input"""
		return value

	def getWeightedValue():
		"""Return the weighted
		value of this input"""
		weight*value

	def setWeight(weight):
		"""Setter for weight
		of this class"""
		self.weight = weight

	def setValue(val):
		"""Setter for value
		of this class"""
		self.value = val

	def getSource():
		"""Return source of
		this input edge"""
		return source

	def getSink():
		"""Return sink of
		this input edge"""
		return sink