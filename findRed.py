import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    #.read() returns two outputs, the later is the frame (image) that we edit
    ret, frame = cap.read()
    #convert to HSV colorspace
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Display before and after frames side by side
    cv2.imshow('before', frame)
    cv2.imshow('after', hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#When finished (q is pressed) release the camera and close windows
cap.release()
cv2.destroyAllWindows()
