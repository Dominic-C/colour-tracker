# colour-tracker

This source code tracks the largest object of a specified colour

## Camera Follower
This source code controls 2 servos, one mounted on top of the other. This allows for the mounted camera to have 2 axis of freedom

## Object tracking
### Requirements:
* opencv 3.4.1
* pyserial

the object tracking file allows the camera (webcam or usb camera) to track an object of a unique colour. You'll have to alter the upper and lower limits of the colour detection parameters to suit the colour you wish to track. (a hot pink postit in my example)

## Picamera object tracking
### Requirements:
* Raspberrypi camera

This combines ideas from the previous 2 source codes. The main idea is to get a raspberrypi camera that is mounted on servos to follow an object of a unique colour. Do note that the upper and lower limits of the colour detection parameters may defer on different cameras, so please check your parameters if there's something wrong.
