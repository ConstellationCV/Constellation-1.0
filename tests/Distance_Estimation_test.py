import sys
sys.path.insert(0, '../src/modules/Position_Estimation')
from Distance import DistanceEstimator

de = DistanceEstimator()
print(de.getListOfDotCoords('../data/image.png', 'dot_pics'))
print len(de.getListOfDotCoords('../data/image.png', 'dot_pics')[0])