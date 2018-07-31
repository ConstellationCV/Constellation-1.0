import numpy as np
class input:
	weight = None
	value = None

	def __init__(self, value):
		self.weight = self.weight = np.random.random_sample()
		self.value = value;

	def getWeight():
		"""Return the weight
		of this input
    	"""
		return weight

	def getValue():
		"""Return the value
		of this input
    	"""
		return value

	def getWeightedValue():
		"""Return the weighted
		value of this input
    	"""
		weight*value

	def setWeight(weight):
		"""Setter for weight
		of this class
    	"""
		self.weight = weight

	def setValue(val):
		"""Setter for value
		of this class
    	"""
		self.value = val