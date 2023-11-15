import cv2
import numpy as np
import hand_tracking_module as htm
import time
import autopy

####################################################
# Parameters ->
wCam, hCam = 1280, 720
frameR = 100 # Frame Reduction # This means that we will be reducing the size of the frame by 100 pixels to obtain the region of interest which will be mapped to the device screen 
smoothening_factor = 7
####################################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

plocX, plocY = 0, 0 # previous location of the mouse
clocX, clocY = 0, 0 # current location of the mouse

detector = htm.handDetector(detectionCon=0.7)

ptime = 0
ctime = 0

#####################################################
# Steps ->
# 1. Find hand landmarks
# 2. Get the tip of the index and middle fingers
# 3. Check which fingers are up
# 4. Only Index Finger : Moving Mode
# 5. Convert Coordinates of the finger tips wrt the frame to the coordinates of the finger tips wrt the screen of the device
# 6. Smoothen Values # This means that we will not be moving the mouse directly to the coordinates of the hand but we will be moving it slowly to the coordinates of the hand by using the previous coordinates of the hand and the current coordinates of the hand so that the mouse movement is smooth and not jerky
# 7. Move Mouse
# 8. Both index and middle finger : Clicking Mode
# 9. Find distance between fingers
# 10. Click mouse if distance short
#####################################################

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1) # flip the image horizontally
    
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img) # step 1
    
    # step 2
    if lmList is not None and len(lmList) != 0:
        x1, y1 = lmList[8][1:] # tip of index finger
        x2, y2 = lmList[12][1:] # tip of middle finger
        print("x1, y1, x2, y2 : ",x1, y1, x2, y2)
        fingers = detector.fingersUp() # step 3
        print("Fingers : ",fingers)
        
        cv2.rectangle(img, (frameR, frameR), (wCam-frameR, hCam-frameR), (255, 0, 255), 2) # draw a rectangle around the region of interest
        
        # step 4
        if fingers[1] == 1 and fingers[2] == 0:
            # step 5
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, autopy.screen.size()[0]))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, autopy.screen.size()[1]))
            
            #step 6
            clocX = plocX + (x3 - plocX) / smoothening_factor
            clocY = plocY + (y3 - plocY) / smoothening_factor
            
            # step 7
            print("Mouse position : ",clocX, clocY)
            autopy.mouse.move(clocX, clocY)
            
            print("Mouse moved")
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED) # draw a circle at the tip of the index finger indicating moving mode
            plocX, plocY = clocX, clocY
            
        #step 8
        if fingers[1] == 1 and fingers[2] == 1:
            # step 9
            length, img, lineInfo = detector.findDistance(8, 12, img)
            print("Length : ",length)
            
            # step 10
            if length < 30:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()
                print("Mouse clicked")
    
    # display the frame rate
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.rectangle(img, (1, 1), (250, 70), (255, 255, 255), cv2.FILLED)
    cv2.putText(img, "FPS : " + str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
    
    # show the image 
    cv2.imshow("Image", img)
    cv2.waitKey(1)
