import sys
sys.path.insert(0, '../src/modules/Feature_Extractor')
from Loc_Extractor import Extractor
from Train import Trainer
sys.path.insert(0, '../src/modules/Prediction_Models')
from KNearestNeighbors import KNN
sys.path.insert(0, '../src/modules/Arithmetic_Toolkit')
from Linear_Algebra import Vectors
import pandas as pd
import numpy as np

class DistanceEstimator:
	def getListOfDotCoords(self, imagePath, dotImagesPath):
		t = Trainer()
		e=Extractor()
		v=Vectors()
		imageTemplateList = t.createListOfImageTemplates("dot", dotImagesPath)
		pts = sorted(e.getMatchingPoints(imagePath, imageTemplateList, 0.9)[0])
		for pt in pts:
			for pt2 in pts[pts.index(pt):]:
				if pt==pt2:
					continue
				else:
					if v.distance(pt,pt2)<10:
						pts.remove(pt2)
		return pts

	def getPtsByDistance(self, list, center):
		v=Vectors()
		return sorted(list, key=lambda(point): v.distance(point, center))

	def getNearestDot(self, imagePath, dotImagesPath,objectCoords):
		return min(self.getPtsByDistance(self.getListOfDotCoords(imagePath, dotImagesPath),objectCoords))

	def getDistanceBWDots(self, imagePath, dotImagesPath, objectCoords):
		by_distance = self.getPtsByDistance(self.getListOfDotCoords(imagePath, dotImagesPath),objectCoords)
		firstDot = min(by_distance)
		by_distance.remove(firstDot)
		secondDot =  min(by_distance)
		v = Vectors()
		return v.distance(firstDot, secondDot)

	def classify(self, distance):
		pointsList = []
		df = pd.read_csv('../datasets/PtsDistance.csv')
		for index, row in df.iterrows():
			tempPoint = []
			tempPoint.append(row[0])
			tempPoint.append(row[1])
			pointsList.append(tempPoint)
		knn = KNN()
		return knn.knn_classify(4, pointsList, distance)















