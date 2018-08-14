import sys
sys.path.insert(0, '../src/drivers') # for your use - path will be "path/to/Constellation/src/drivers"
from Object_Detection import Detector

d = Detector(["../data/object_videos/cube1.mov","../data/object_videos/cube2.mov","../data/object_videos/cube4.mov","../data/object_videos/sphere1.mov","../data/object_videos/cube3.mov"],["cube","cube","cube","sphere","cube"])
print(d.getObjectCoordinates("../data/image.png","cube",0.7))
print(d.getObjectCoordinates("../data/image.png","sphere",0.7))