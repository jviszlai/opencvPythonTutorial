import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    #.read() returns two outputs, the later is the frame (image) that we edit
    ret, frame = cap.read()
    #convert to HSV colorspace
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Define range of colors to be selected
    lowerRed1 = np.array([170, 175, 0])
    upperRed1 = np.array([180, 255, 100])

    lowerRed2 = np.array([0, 175, 0])
    upperRed2 = np.array([10, 255, 100])
    #Filter the frame to only keep colors in the range
    mask1 = cv2.inRange(hsv, lowerRed1, upperRed1)
    mask2 = cv2.inRange(hsv, lowerRed2, upperRed2)
    mask = mask1 + mask2
    #Erode and dilate the image to minimize small errors
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    #Sort out all the different shapes that are in the range, and color them red
    mask, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #find biggest area
    biggestArea = 0
    biggestContour = None
    for c in contours:
        if cv2.contourArea(c) > biggestArea:
            biggestArea = cv2.contourArea(c)
            biggestContour = c
    #Removes all other contours and keeps biggest contour
    for c in contours:
        if c is not biggestContour:
            cv2.drawContours(mask, [c], -1, 0, -1)

    cv2.drawContours(mask, [biggestContour], 0, (180,200,200), 3)
    #Combine the mask with original frame to only show desired object
    res = cv2.bitwise_and(frame,frame, mask= mask)
    #Display before and after frames side by side
    cv2.imshow('before', frame)
    cv2.imshow('after', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#When finished (q is pressed) release the camera and close windows
cap.release()
cv2.destroyAllWindows()
