import sys
sys.path.insert(0, '../src/modules/Feature_Extractor')
from Loc_Extractor import Extractor
from Train import Trainer

class DistanceEstimator:
	def getListOfDotCoords(self, imagePath, dotImagesPath):
		t = Trainer()
		imageTemplateList = t.createListOfImageTemplates("dot", dotImagesPath)
		return getMatchingPoints(imagePath, imageTemplateList, 0.7)
	def 