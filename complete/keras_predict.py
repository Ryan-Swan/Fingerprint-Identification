from keras.models import load_model
from keras.models import Sequential
import os
import numpy as np 
from keras.layers import Activation, Dropout, Flatten, Dense, BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras import optimizers
import cv2


img_width, img_height = 300, 400

model = Sequential()
model.add(Convolution2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 1)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Convolution2D(64, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Convolution2D(128, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Convolution2D(256, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))


model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model = load_model('model.h5')
			  
img = cv2.imread('test.jpg')
img = cv2.resize(img,(300,400))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = np.reshape(img,[1,300,400,1])
img = img / 255

classes = model.predict_classes(img)

print (classes)