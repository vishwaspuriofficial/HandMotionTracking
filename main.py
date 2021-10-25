#Title: Program 17:  Tutorial
#Developer: Vishwas Puri
#Purpose: a program that finds the 22 points located in your hands using machine learning dataset and algoritm from mediapipe made by google.
#To capture photo show a peace sign and it will autoclick photo
import threading
from datetime import datetime
import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
import random
import os
pTime = 0
cTime = 0
try:
    try:
        try:
            cap = cv2.VideoCapture(0)
        except:
            cap = cv2.VideoCapture(1)
    except:
        cap = cv2.VideoCapture(2)
except:
    "Camera couldn't be turned on!"

detector = htm.handDetector()
tipsIds = [8,12]


def filename():
    i = random.randint(1, 100000000000000)
    check = str(i)+".jpg"
    if check in os.listdir():
        filename()
    else:
        return i

a = True
while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=False )
    lmList = detector.findPosition(img, draw=False)
    cv2.putText(img, str("Show peace sign to click a photo"), (10, 70), cv2.FONT_HERSHEY_PLAIN, 2 , (255, 0, 255), 3)
    def photo():
        if len(lmList) != 0:
            #if lmList[4][2]<lmList[3][2] and lmList[8][2]<lmList[6][2] and lmList[12][2]<lmList[10][2] and lmList[16][2]<lmList[14][2] and lmList[20][2]<lmList[18][2]:
                # Check if hand is open
               # print("Hand Open")
            if lmList[8][2]<lmList[6][2] and lmList[12][2]<lmList[10][2] and lmList[16][2]>lmList[14][2] and lmList[20][2]>lmList[18][2]:
                            #Check if index and middle finder are open
                #print("Finger Open")
                i = filename()
                img_name = "{}.jpg".format(i)
                cv2.imwrite(img_name, img)
                print("{} written!".format(img_name))
                time.sleep(1)
    photo()
            #cv2.putText(img, str("Cheese!!!"), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

            #continue



    # cTime = time.time()
    # fps = 1 / (cTime - pTime)
    # pTime = cTime
    cv2.imshow("Image", img)
    cv2.waitKey(1)

