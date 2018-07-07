from collections import deque
import numpy as np
import cv2
import imutils

pinkLower = np.array([145, 100, 80])
pinkUpper = np.array([165, 255, 255])

cap = cv2.VideoCapture(0)

img = cap.read()[1]
height, width, channels = img.shape
print("height: {}, width: {}".format(height, width))

while(True):

    ret, frame = cap.read()

    # frame = imutils.resize(frame, width = 600)
    blurred = cv2.GaussianBlur(frame, (11,11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, pinkLower, pinkUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)


    

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    center = None
    
    if len(cnts) > 0:

        c = max(cnts, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        M = cv2.moments(c)
        center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))

        if w > 10 and h > 10:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.circle(frame, (center), 2, (255, 255, 255), -1)
    else:
        center = (int(width/2), int(height/2))

    # drawing lines for visualis
    cv2.line(frame, (int(width/2 + 30), 0), (int(width/2 + 30), height), (255, 0, 127), 1)
    cv2.line(frame, (int(width/2 - 30), 0), (int(width/2 - 30), height), (255, 0, 127), 1)
    cv2.line(frame, (0, int(height/2 + 30)), (width, int(height/2 + 30)), (255, 0, 127), 1)
    cv2.line(frame, (0, int(height/2 - 30)), (width, int(height/2 - 30)), (255, 0, 127), 1)

    cv2.line(frame, center, (int(width/2), int(height/2)), (0, 255, 255), 1)

    cv2.imshow("mask", mask)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.release()
cv2.destroyAllWindows()