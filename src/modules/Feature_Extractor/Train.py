import cv2
import numpy as np
import os
import math

class Trainer:
    def createAllFrameImages(self, videoFileName, outFolderPath):
        # Playing video from file:
        cap = cv2.VideoCapture(videoFileName)

        try:
            if not os.path.exists(outFolderPath):
                os.makedirs(outFolderPath)
        except OSError:
            print ('Error: Creating directory of data')

        currentFrame = 0
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Saves image of the current frame in jpg file
            name = outFolderPath + '/frame' + str(currentFrame) + '.png'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)

            # To stop duplicate images
            currentFrame += 1

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    def createIntervalFrameImages(self, videoFileName, outFolderPath, objectName):
        videoFile = videoFileName
        imagesFolder = outFolderPath
        try:
            if not os.path.exists(outFolderPath):
                os.makedirs(outFolderPath)
        except OSError:
            print ('Error: Creating directory of data')
        cap = cv2.VideoCapture(videoFile)
        frameRate = cap.get(5) #frame rate
        print frameRate
        while(cap.isOpened()):
            frameId = cap.get(1) #current frame number
            ret, frame = cap.read()
            if (ret != True):
                break
            if (frameId % math.floor(frameRate) == 10 or frameId % math.floor(frameRate) == 20 or frameId % math.floor(frameRate) == 30
                or frameId % math.floor(frameRate) == 40 or frameId % math.floor(frameRate) == 50):
                filename = imagesFolder + "/" + objectName + "_image_" +  str(int(frameId)) + ".png"
                cv2.imwrite(filename, frame)
        cap.release()
        print "Done!"

    def createListOfImageNames(self, directoryName, objectName):
        list = []
        for filename in os.listdir(directoryName):
            if objectName in filename:
                list.append(directoryName)
            else:
                continue
        return list

    def createListOfImageTemplates(self, listOfNames, imageStorageDirectoryPath):
        list = []
        for name in listOfNames:
            list.append(cv2.cvtColor(cv2.imread(imageStorageDirectoryPath + name),cv2.COLOR_BGR2GRAY))
        return list

    def trainOnImages(self, pathToImageFolder):
        #create templates to match to
        print("not yet implemented")


#t = Trainer()
#t.createAllFrameImages('shorter.mov')
