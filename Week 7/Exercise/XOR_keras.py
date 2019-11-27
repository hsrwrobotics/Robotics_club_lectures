# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:34:47 2019

@author: batho
"""

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD



x_train=np.array([[0,0],
                 [0,1],
                 [1,0],
                 [1,1]])
y_train=np.array([[0],[1],[1],[0]])

model=Sequential()
num_neurons=10
model.add(Dense(num_neurons, input_dim=2))
model.add(Activation('tanh'))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.summary()

sgd=SGD(lr=.1)
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])

model.predict(x_train)

model.fit(x_train, y_train, epochs=1000)

model.predict_classes(x_train)

model.predict(x_train)