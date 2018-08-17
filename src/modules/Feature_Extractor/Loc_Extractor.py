import cv2
import numpy as np
import json
import time
import sys
sys.path.insert(0, '../src/exceptions')
from CannotMatchError import CannotMatchError

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
		try:
			return self.findMiddle(min(self.getMatchingPoints(imagePath,templateList,confidenceThreshold)))
		except Exception as e:
			raise ValueError('Cannot match object anywhere in image')
		
	def findMiddle(self, input_list):
		middle = float(len(input_list))/2
		if middle % 2 != 0:
			return input_list[int(middle - .5)]
		else:
			return (input_list[int(middle)], input_list[int(middle-1)])

	def getMatchingPoints(self, imagePath, templateList, confidenceThreshold):
		list = []
		img_rgb = cv2.imread(imagePath)
		image = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
		#start = time.time()
		for template in templateList:
			templateList = []
			matches = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
			w,h = template.shape[::-1]
			loc = np.where(matches>=confidenceThreshold)
			for pt in zip(*loc[::-1]):
				pointtpl = (pt[0]+(w/2),pt[1]+(h/2))
				templateList.append(pointtpl)
			list.append(templateList)
		#end = time.time()
		#print(end-start)
		return self.cleanList(list)

	def cleanList(self, list):
		list2 = [x for x in list if x]
		return sorted(list2)