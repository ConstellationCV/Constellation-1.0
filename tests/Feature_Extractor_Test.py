import sys
sys.path.insert(0, '/Users/prathamgandhi/Desktop/constellation/Constellation/src/modules/Feature_Extractor')
from Train import Trainer
from Loc_Extractor import Extractor

e = Extractor()
t = Trainer()
t.createIntervalFrameImages("../data/test.mov", "out_dir", "cube")
templateList = t.createListOfImageTemplates(t.createListOfImageNames("out_dir", "cube"), "out_dir")