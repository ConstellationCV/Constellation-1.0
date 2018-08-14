import sys
sys.path.insert(0, '../src/modules/Feature_Extractor')
from Train import Trainer
from Loc_Extractor import Extractor

e = Extractor()
t = Trainer()
t.createIntervalFrameImages("../data/object_videos/cube1.mov", "out_dir", "cube","1")
#t.createIntervalFrameImages("../data/object_videos/sphere1.mov", "out_dir", "sphere","1")
#t.createIntervalFrameImages("../data/object_videos/sphere2.mov", "out_dir", "sphere","2")
cubeTemplateList = t.createListOfImageTemplates("cube", "out_dir")
#templateListList = [cubeTemplateList,sphereTemplateList]
print e.getObjectLoc("../data/image.png", cubeTemplateList, 0.7)
#e.getObjectLoc( "../data/cube.png", cubeTemplateList, 0.8)
#print e.findAllObjects("../data/both_alt_env.png",templateListList, 0.8)
