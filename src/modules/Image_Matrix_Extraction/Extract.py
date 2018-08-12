import cv2
import numpy as np

img_rgb = cv2.imread('test_1.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template0 = cv2.cvtColor(cv2.imread("cube0.png"),cv2.COLOR_BGR2GRAY)
template1 = cv2.cvtColor(cv2.imread("cube1.png"),cv2.COLOR_BGR2GRAY)
template2 = cv2.cvtColor(cv2.imread("cube2.png"),cv2.COLOR_BGR2GRAY)
template3 = cv2.cvtColor(cv2.imread("cube3.png"),cv2.COLOR_BGR2GRAY)
template4 = cv2.cvtColor(cv2.imread("cube4.png"),cv2.COLOR_BGR2GRAY)
template5 = cv2.cvtColor(cv2.imread("cube5.png"),cv2.COLOR_BGR2GRAY)
template6 = cv2.cvtColor(cv2.imread("cube6.png"),cv2.COLOR_BGR2GRAY)
template7 = cv2.cvtColor(cv2.imread("cube7.png"),cv2.COLOR_BGR2GRAY)
template8 = cv2.cvtColor(cv2.imread("cube8.png"),cv2.COLOR_BGR2GRAY)

test0 = cv2.cvtColor(cv2.imread("test0.png"),cv2.COLOR_BGR2GRAY)

resMed = cv2.matchTemplate(img_gray,template5,cv2.TM_CCOEFF_NORMED)
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

