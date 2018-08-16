import sys
sys.path.insert(0, '../src/modules/Feature_Extractor')
from Loc_Extractor import Extractor
from Train import Trainer
sys.path.insert(0, '../src/modules/Prediction_Models')
from KNearestNeighbors import KNN

class DistanceEstimator:
	def getListOfDotCoords(self, imagePath, dotImagesPath):
		t = Trainer()
		e=Extractor()
		imageTemplateList = t.createListOfImageTemplates("dot", dotImagesPath)
		return e.getMatchingPoints(imagePath, imageTemplateList, 0.9669)
	def getNearestDot(self):
		print("hi")