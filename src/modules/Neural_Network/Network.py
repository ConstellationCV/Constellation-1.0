from Neuron import Neuron
from Input import Input
class Network:
	inputLayer = []
	hiddenLayer1 = []
	hiddenLayer2 = []
	hiddenLayer3 = []
	outputLayer = []
	labeledFeatures = None
	trainingLabels = None
	predictionFeatures = None

	def __init__(labFeats, trainLabs, pred):
		inputLayer.append(Neuron([Input(),Input(),Input(),Input(),Input(),Input(),Input(),Input(),Input(),Input()]))

	def backpropagate():
		for trainLab in trainingLabels:
			for o in outputLayer:
				for inp in o.getInputs():
					db = trainingLabels[trainingLabels.index(o)]
