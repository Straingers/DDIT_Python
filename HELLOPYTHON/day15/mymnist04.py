from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical
import numpy as np
import cv2

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

img = test_images

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
# test_labels = to_categorical(test_labels)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, batch_size=128)

predictions = model.predict(test_images)

right_cnt = 0
miss_cnt = 0

for idx, i in enumerate(predictions):
    if np.argmax(i) != test_labels[idx]:
        cv2.imwrite("miss/" + str(np.argmax(i)) + "_" + str(test_labels[idx]) + "_" + str(idx) + '.jpg', img[idx])
        miss_cnt += 1
    else:
        right_cnt += 1
        
print("맞은 갯수 :", right_cnt)
print("틀린 갯수 :", miss_cnt)
