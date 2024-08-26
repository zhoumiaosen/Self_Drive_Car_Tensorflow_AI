# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 00:02:37 2022

@author: miaosenzhou
"""
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import keras
from keras.models import Sequential 
from keras.layers import Conv2D
from keras.layers import MaxPool2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
import sys
import warnings


if not sys.warnoptions:
    warnings.simplefilter("ignore")

print ("Packages Import: DONE")
#with tf.device('/gpu:0'):
trdate = ImageDataGenerator()
traindata = trdate.flow_from_directory(directory = 'path/DIR', target_size=(64,64))

tsdate = ImageDataGenerator()
testdata = tsdate.flow_from_directory(directory ='path/test/', target_size=(64,64))

image_size = 64

model = keras.models.Sequential()

initializers = {}

model.add( keras.layers.Conv2D(24, 5, input_shape=(64,64,3), activation='relu', ))
model.add( keras.layers.MaxPooling2D(2) )
model.add( keras.layers.Conv2D(48, 5, activation='relu', ))
model.add( keras.layers.MaxPooling2D(2) )
model.add( keras.layers.Conv2D(96, 5, activation='relu', ))
model.add( keras.layers.Flatten() )
model.add( keras.layers.Dropout(0.9) )
model.add(keras.layers.Dense(500, activation='relu',))
model.add(keras.layers.Dense(500, activation='relu',))
model.add(keras.layers.Dense(500, activation='relu',))
model.add(keras.layers.Dense(500, activation='relu',))
model.add(keras.layers.Dense(500, activation='relu',))
model.add( keras.layers.Dense(4, activation='softmax',))

model.summary()
model.compile(loss='binary_crossentropy',
              optimizer = 'adam',
              metrics=['acc'])


from keras.callbacks import ModelCheckpoint, EarlyStopping

with tf.device('/gpu:0'):
    history = model.fit_generator(
    traindata, 
    validation_data = testdata,
    workers=10,
    epochs=200,
)


model.save('car_drive_Sep_26_2023_V5.h5')

def plot_history(history, yrange):
    '''Plot loss and accuracy as a function of the epoch,
    for the training and validation datasets.
    '''
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    # Get number of epochs
    epochs = range(len(acc))

    plt.figure(figsize=(16,9))
    # Plot training and validation accuracy per epoch
    plt.plot(epochs, acc)
    plt.plot(epochs, val_acc)
    plt.title('Training and validation accuracy')
    plt.ylim(yrange)
    
    # Plot training and validation loss per epoch
    plt.figure()
    plt.figure(figsize=(16,9))

    plt.plot(epochs, loss)
    plt.plot(epochs, val_loss)
    plt.title('Training and validation loss')
    
    plt.show()
    
plot_history(history, (0.65, 1.))


