import cv2
import numpy as np

class Extractor:
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