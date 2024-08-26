# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 13:18:35 2022

@author: miaosen
"""

from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image


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

#model = keras.models.load_model('path/models/car_drive_v2.h5')

model.load_weights('path/models/car_drive_v2.h5')

def evaluate(img_fname):
    img = image.load_img(img_fname, target_size=(64, 64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)
    
    # print the probability and category name for the 5 categories 
    # with highest probability: 
    print('Predicted:', preds[0].argmax())
    plt.imshow(img)
    
evaluate('path/name.jpg')