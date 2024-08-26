#!/usr/bin/env python
import cv2
import numpy as np
import Motor
import time
import RPi.GPIO as gpio
import os
import uuid
import time


if __name__ =="__main__":
    print('start capture image')

    video = cv2.VideoCapture(0)
    while True:
        DIR = input("Enter DIR: ")
        success, image = video.read()
            # We are using Motion JPEG, but OpenCV defaults to capture raw images,
            # so we must encode it into JPEG in order to correctly display the
            # video stream.
        image = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
        ret, jpeg = cv2.imencode('.jpg', image)
        path = '/home/pi/Desktop/Pi/AI_Car/DIR'
        uu_id= str(uuid.uuid4())
        filename = DIR + '_' + uu_id+ '.jpg'
        path = path + '/' + DIR
        cv2.imwrite(os.path.join(path,filename),image)
        print (DIR)
        
        try: 
            if DIR == 'w':
                Motor.forward()
            elif DIR == 's':
                Motor.backward()
            elif DIR == 'a':
                Motor.left(30)
            elif DIR == 'd':
                Motor.right(30)
            else:
                print ('NOT Work')
        except:
                pass
        

                
