from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import serial

ser = serial.Serial("/dev/ttyUSB0", 9600)
width, height = 432, 240

camera = PiCamera()
camera.resolution = (width, height)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size = (width , height))

time.sleep(2)


pinkLower = np.array([145, 80, 50])
pinkUpper = np.array([249, 255, 255])

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port="True"):

    image = frame.array
    image = cv2.flip(image,0)
    image = cv2.flip(image,1)

    blurred = cv2.GaussianBlur(image, (11,11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, pinkLower, pinkUpper)
    mask = cv2.erode(mask, None, iterations= 2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[1]

    if len(cnts) > 0:

        c = max(cnts, key=cv2.contourArea)
        x, y, w,h = cv2.boundingRect(c)
        M = cv2.moments(c)
        center = (int(x+w/2), int(y+h/2))
        if w > 10 and h > 10:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.circle(image, center, 2, (255,255,255), -1)
    else:
        center = (width/2, height/2)
    
    x_magnitude = center[0] - width/2
    y_magnitude = height/2 - center[1]
    print("x: {}, y: {}".format(x_magnitude, y_magnitude))
    
    if x_magnitude < -15:
        ser.write('j'.encode())
    if x_magnitude > 15:
        ser.write('l'.encode())
    if y_magnitude < -15:
        ser.write(','.encode())
    if y_magnitude > 15:
        ser.write('i'.encode())

    cv2.imshow("frame", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)


    if key == ord("q"):
        break
