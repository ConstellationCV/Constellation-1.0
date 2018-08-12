import sys
import json
sys.path.insert(0, '../src/modules/Feature_Extractor')
from Train import Trainer
from pprint import pprint
from Loc_Extractor import Extractor

e = Extractor()
t = Trainer()
t.createIntervalFrameImages("../data/object_videos/cube1.mov", "out_dir", "cube","1")
t.createIntervalFrameImages("../data/object_videos/cube2.mov", "out_dir", "cube","2")
t.createIntervalFrameImages("../data/object_videos/cube3.mov", "out_dir", "cube","3")
t.createIntervalFrameImages("../data/object_videos/cube4.mov", "out_dir", "cube","4")
t.createIntervalFrameImages("../data/object_videos/sphere1.mov", "out_dir", "sphere","1")
t.createIntervalFrameImages("../data/object_videos/sphere2.mov", "out_dir", "sphere","2")
cubeTemplateList = t.createListOfImageTemplates("cube", "out_dir")
sphereTemplateList = t.createListOfImageTemplates("sphere", "out_dir")
templateListList = [cubeTemplateList,sphereTemplateList]
#print e.getObjectLoc( "../data/cube.png", cubeTemplateList, 0.8)
print e.findAllObjects("../data/both_alt_env.png",templateListList, 0.8)
