'''
Using OpenCV takes a mp4 video and produces a number of images.
Requirements
----
You require OpenCV 3.2 to be installed.
Run
----
Open the main.py and edit the path to the video. Then run:
$ python main.py
Which will produce a folder called data with the images. There will be 2000+ images for example.mp4.
'''
import cv2
import numpy as np
import os

import cv2
import math

videoFile = "test.mov"
imagesFolder = "images_out"
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
        filename = imagesFolder + "/image_" +  str(int(frameId)) + ".png"
        cv2.imwrite(filename, frame)
cap.release()
print "Done!"



class Train:
    def createFrameImages(self, videoFileName):
        # Playing video from file:
        cap = cv2.VideoCapture(videoFileName)

        try:
            if not os.path.exists('data'):
                os.makedirs('data')
        except OSError:
            print ('Error: Creating directory of data')

        currentFrame = 0
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Saves image of the current frame in jpg file
            name = 'data/frame' + str(currentFrame) + '.png'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)

            # To stop duplicate images
            currentFrame += 1

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
    def trainOnImages(pathToImageFolder):
        print("not yet implemented")

#t = Train()
#t.createFrameImages('shorter.mov')
