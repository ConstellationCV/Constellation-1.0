import sys
sys.path.insert(0, '../src/modules/Feature_Extractor')
from Loc_Extractor import Extractor
from Train import Trainer
sys.path.insert(0, '../src/modules/Prediction_Models')
from Train import Trainer
sys.path.insert(0, '../src/modules/Arithmetic_Toolkit')
from Linear_Algebra import Vectors

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
		return sorted(list, key=lambda (point): v.distance(point, center))

	def getNearestDot(self, imagePath, dotImagesPath,objectCoords):
		return min(self.getPtsByDistance(self.getListOfDotCoords(imagePath, dotImagesPath),objectCoords))