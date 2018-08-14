import cv2
import numpy as np
import os
import math
import json

class Trainer:
    def createAllFrameImages(self, videoFileName, outFolderPath):
        # Playing video from file:
        outFolderPath = "../data/"+outFolderPath
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

    def createIntervalFrameImages(self, videoFileName, outFolderPath, objectName, objectID):
        videoFile = videoFileName
        outFolderPath = "../data/"+outFolderPath
        imagesFolder = outFolderPath
        try:
            if not os.path.exists(outFolderPath):
                os.makedirs(outFolderPath)
        except OSError:
            print ('Error: Creating directory of data')
        alreadyDone = False
        for filename in os.listdir("../data/"+outFolderPath):
            if objectName + "_" + objectID in filename:
                alreadyDone=True
                break
        if not alreadyDone:
            cap = cv2.VideoCapture(videoFile)
            frameRate = cap.get(5) #frame rate
            while(cap.isOpened()):
                frameId = cap.get(1) #current frame number
                ret, frame = cap.read()
                if (ret != True):
                    break
                if (frameId % math.floor(frameRate) == 10 or frameId % math.floor(frameRate) == 50):
                    filename = imagesFolder + "/" + objectName + "_" + objectID + "_image_" +  str(int(frameId)) + ".png"
                    cv2.imwrite(filename, frame)
            cap.release()

    def createListOfImageNames(self, directoryName, objectName):
        list = []
        directoryName = "../data/"+directoryName
        for filename in os.listdir(directoryName):
            if objectName in filename:
                list.append(filename)
            else:
                continue
        return list

    def createListOfImageTemplates(self, objectName, imageStorageDirectoryPath):
        list = []
        listOfNames = self.createListOfImageNames(imageStorageDirectoryPath, objectName)
        imageStorageDirectoryPath = "../data/"+imageStorageDirectoryPath+"/"
        for name in listOfNames:
            list.append(cv2.cvtColor(cv2.imread(imageStorageDirectoryPath + name),cv2.COLOR_BGR2GRAY))
        with open('../data/DO_NOT_TOUCH/indexed_objects.json') as f:
            data = json.load(f)
        lastKey = -1
        alreadyIn = False
        for key in data:
            lastKey = int(key)
            if data[key] == objectName:
                alreadyIn = True
        if not alreadyIn:
            newKey = str(lastKey+1)
            a_dict = {newKey:objectName}
            data.update(a_dict)
            with open('../data/DO_NOT_TOUCH/indexed_objects.json', 'w') as f:
                json.dump(data, f)
        return list
