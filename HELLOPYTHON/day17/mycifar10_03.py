import numpy as np
from tensorflow.keras import datasets, layers, models
import cv2
 
cifar10 = datasets.cifar10 
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
 
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
 
train_images_refine = train_images.reshape((50000, 32, 32, 3))
test_images_refine = test_images.reshape((10000, 32, 32, 3))

train_images_refine = train_images / 255.0
test_images_refine = test_images / 255.0

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
 
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
 
model.fit(train_images_refine, train_labels, epochs=10)

img = cv2.imread("dog.jpg")
img = cv2.resize(img, dsize=(32, 32))
cv2.imshow("My Image", img)
cv2.imshow("Test Image", test_images[0])
img = img / 255.0
img = img.reshape(1, 32, 32, 3)

predictions = model.predict(img)

print(np.argmax(predictions))

cv2.waitKey(0)
cv2.destroyAllWindows()
 