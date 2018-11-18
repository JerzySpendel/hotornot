from loader import dogs_and_hotdogs, common_size

from keras import layers, models
from sklearn.utils import shuffle
import numpy as np

dogs, hotdogs = dogs_and_hotdogs()
dogs_len = len(dogs)
hotdogs_len = len(hotdogs)

X_train = np.vstack((
    dogs,
    hotdogs
))
Y_train = np.vstack((
    np.array([[1, 0]] * dogs_len),
    np.array([[0, 1]] * hotdogs_len)
))

X_train, Y_train = shuffle(X_train, Y_train)
X_train = X_train.astype('float32')
Y_train = Y_train.astype('float32')

X_train /= 255
Y_train /= 255

input_shape = common_size + (3,)

model = models.Sequential()
model.add(layers.Conv2D(64, (5, 5), activation='relu', input_shape=input_shape))
model.add(layers.MaxPooling2D((2, 2), strides=(2, 2)))
model.add(layers.Conv2D(64, (5, 5), activation='relu'))
model.add(layers.MaxPooling2D((2, 2), strides=(2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(2500, activation='relu'))
model.add(layers.Dropout(0.3))
model.add(layers.Dense(100, activation='relu'))
model.add(layers.Dense(2, activation='softmax'))


model.compile(optimizer='sgd',
              loss='categorical_crossentropy',
              metrics=['accuracy']
              )

model.fit(X_train, Y_train, epochs=2000, batch_size=32)
import pdb; pdb.set_trace()