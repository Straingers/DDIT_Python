import tensorflow as tf
import numpy as np
import cv2

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images_refine = train_images / 255.0
test_images_refine = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images_refine, train_labels, epochs=10)

predictions = model.predict(test_images_refine)

cnt_o = 0
cnt_x = 0

for idx, img in enumerate(predictions):
    if np.argmax(img) != test_labels[idx]:
        cv2.imwrite("image_miss/" + str(np.argmax(img)) + "_" + str(test_labels[idx]) + "_" + str(idx) + '.jpg', test_images[idx])
        cnt_o += 1
    else:
        cnt_x += 1
        
cv2.waitKey(0)
cv2.destroyAllWindows()

print("맞은 갯수 :", cnt_o)
print("틀린 갯수 :", cnt_x)
