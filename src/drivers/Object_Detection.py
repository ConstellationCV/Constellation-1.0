import sys
sys.path.insert(0, '../src/modules/Feature_Extractor')
from Loc_Extractor import Extractor
from Train import Trainer
class Detector:
	def __init__(self, videoPaths, objectNames):
		#self.imagePath = imagePath
		self.objectNames = objectNames
		e = Extractor()
		t = Trainer()
		objectIndex = 0
		numTimesObjectVidDissected = {}
		for path in videoPaths:
			if objectNames[objectIndex] not in numTimesObjectVidDissected:
				numTimesObjectVidDissected[objectNames[objectIndex]] = "0"
			t.createIntervalFrameImages(path, "training_images_from_videos", objectNames[objectIndex],numTimesObjectVidDissected[objectNames[objectIndex]])
			numTimesObjectVidDissected[objectNames[objectIndex]] = str(int(numTimesObjectVidDissected[objectNames[objectIndex]])+1)
			objectIndex += 1
		for o in objectNames:
			exec("self."+o+"TemplateList=t.createListOfImageTemplates('"+o+"', 'training_images_from_videos')")

	def getObjectCoordinates(self, imagePath, objectName, confidenceRequirement):
		exec("templateList = self."+objectName+"TemplateList")
		e = Extractor()
		return e.getObjectLoc(imagePath,templateList, confidenceRequirement)