import sys
sys.path.insert(0, '../src/modules/Position_Estimation')
from Distance import DistanceEstimator
sys.path.insert(0, '../src/drivers') # for your use - path will be "path/to/Constellation/src/drivers"
from Object_Detection import Detector

d = Detector(["../data/object_videos/cube1.mov","../data/object_videos/cube2.mov","../data/object_videos/cube4.mov","../data/object_videos/cube3.mov"],["cube","cube","cube","cube"])
cubeCoords = (d.getObjectCoordinates("../data/image.png","cube",0.7))
print cubeCoords
# print(d.getObjectCoordinates("../data/image.png","sphere",0.7))

de = DistanceEstimator()
#print(de.getListOfDotCoords('../data/imageDots.png', 'dot_pics'))

print(de.getNearestDot('../data/imageDots.png', 'dot_pics',cubeCoords))
#print len(de.getListOfDotCoords('../data/imageDots.png', 'dot_pics'))