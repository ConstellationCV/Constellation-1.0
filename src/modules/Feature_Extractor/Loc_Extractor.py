import cv2
import numpy as np
import json

class Extractor:
	def findAllObjects(self, imagePath, templateListList, confidenceThreshold):
		objsDict = dict()
		templateListListIndex = 0
		with open('../data/DO_NOT_TOUCH/indexed_objects.json') as f:
			data = json.load(f)
		for key in sorted(data):
			tempObjectName = data[key]
			objsDict[tempObjectName] = self.getObjectLoc(imagePath, templateListList[int(key)], confidenceThreshold)
			templateListListIndex = templateListListIndex+1
		return objsDict

	def getObjectLoc(self, imagePath, templateList, confidenceThreshold):
		return min(min(self.getMatchingPoints(imagePath,templateList,confidenceThreshold)))

	def getMatchingPoints(self, imagePath, templateList, confidenceThreshold):
		list = []
		img_rgb = cv2.imread(imagePath)
		image = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
		for template in templateList:
			templateList = []
			matches = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
			w,h = template.shape[::-1]
			loc = np.where(matches>=confidenceThreshold)
			for pt in zip(*loc[::-1]):
				pointtpl = (pt[0]+(w/2),pt[1]+(h/2))
				templateList.append(pointtpl)
			list.append(templateList)
		return self.cleanList(list)

	def cleanList(self, list):
		list2 = [x for x in list if x]
		return list2