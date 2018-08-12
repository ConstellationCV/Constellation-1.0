import cv2
import numpy as np

"""
img_rgb = cv2.imread('test_1.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
test0 = cv2.cvtColor(cv2.imread("test0.png"),cv2.COLOR_BGR2GRAY)

resMed = cv2.matchTemplate(img_gray,test0,cv2.TM_CCOEFF_NORMED)
wm, hm = template0.shape[::-1]
threshold = 0.9
loc = np.where( resMed >= threshold)
for pt in zip(*loc[::-1]):
	print(pt)
	pointtpl = (pt[0]+(wm/2),pt[1]+(hm/2))
	print(pointtpl)
	cv2.rectangle(img_rgb, pt, (pt[0] + wm, pt[1] + hm), (47,255,173), 2)
	cv2.rectangle(img_rgb, pointtpl, pointtpl, (0,0,255), 4)

cv2.imshow('Detected',img_rgb)
if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
cv2.imwrite('outputMatches1.png',img_rgb)
"""

class Extractor:
	def getMatchingPoints(self, imagePath, templateList, confidenceThreshold):
		list = []
		img_rgb = cv2.imread(imagePath)
		image = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
		for template in templateList:
			matches = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
			w,h = template.shape[::-1]
			loc = np.where(matches>=confidenceThreshold)
			for pt in zip(*loc[::-1]):
				pointtpl = (pt[0]+(w/2),pt[1]+(h/2))
				list.append(pointtpl)
		return list
