#!/usr/bin/env python
import cv2
import numpy as np
import Motor
import time
import RPi.GPIO as gpio
import os
import uuid
import time
import tensorflow as tf

from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image
#from tensorflow.keras.preprocessing import image



def evaluate(model,img_fname):
    img = cv2.resize(img_fname,(64,64))
    x = np.array(img)
    #x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)
    
    # print the probability and category name for the 5 categories 
    # with highest probability: 
    # print('Predicted:', preds[0].argmax())
    return(preds[0].argmax())
    

if __name__ =="__main__":
    print('start capture image')
    
    #model = keras.models.load_model('path/models/car_drive_v2.h5', compile = False)
    video = cv2.VideoCapture(0)
    model = keras.models.Sequential([
    
    keras.layers.Conv2D(filters=64,kernel_size =  3, strides=1 ,padding="same", activation='relu',input_shape = (64,64,3)),
    keras.layers.Dropout(0.25),
    keras.layers.MaxPooling2D((2,2)),
        
    keras.layers.Conv2D(filters=128,kernel_size =  3, strides=1 ,padding="same" ,activation='relu'),
    keras.layers.Dropout(0.25),
    keras.layers.MaxPooling2D((2, 2)),
    
    keras.layers.Conv2D(filters=256,kernel_size =  3, strides=1 ,padding="same" ,activation='relu'),
    keras.layers.Dropout(0.25),
    keras.layers.MaxPooling2D((2, 2)),

    keras.layers.Flatten(),

    keras.layers.Dense(512, activation="relu"),
    keras.layers.Dropout(0.25),
    keras.layers.Dense(4, activation='sigmoid')
    ])



    model.load_weights('path/models/car_drive_v3.h5')
    
    while True:
        success, image_1 = video.read()
            # We are using Motion JPEG, but OpenCV defaults to capture raw images,
            # so we must encode it into JPEG in order to correctly display the
            # video stream.
        try: 
            image_1 = cv2.rotate(image_1, cv2.cv2.ROTATE_90_CLOCKWISE)
            DIR = evaluate(model,image_1)
            print (DIR)
            
            if DIR == 3:
                Motor.forward()
                print ('w')
            elif DIR == 2:
                Motor.backward()
                print ('s')
            elif DIR == 0:
                Motor.left(30)
                print ('a')
            elif DIR == 1:
                Motor.right(30)
                print ('d')
            else:
                print ('NOT Work')
        
        except:
                pass
        

                
