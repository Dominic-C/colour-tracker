# Colour Tracking (OpenCV)
The colour tracker repository aims to provide basic examples of using opencv. Use cases here include colour tracking and object following via colour tracking.

## Camera Follower
### Requirements:
* OpenCV 3.4.1
* pyserial for python3
* Arduino and 2 servos
* RaspberryPi camera and RaspberryPi

Contains source code for an an Arduino which takes in serial input. The accompanying python code would run on a raspberry pi or any computer with opencv installed.

**concept:**
1. The camera masks out a unique colour (hot pink in my example) and creates a border around it with OpenCV.

<img src=Images/Mask.png width=400>

2. If the center of the border is not in a specified region on the screen, serial input will be sent to the arduino. The arduino recieves these signals and moves the camera to center the object.

<img src=Images/Guidelines.png width=400>

Purple lines illustrate the boundary at which the camera considers an object centered.

## Object Tracking
### Requirements:
* OpenCV 3.4.1

Contains the basic implementation for colour tracking, tested on a laptop. Uses the same processes to recognize objects, but no arduino and camera movement capabilities.