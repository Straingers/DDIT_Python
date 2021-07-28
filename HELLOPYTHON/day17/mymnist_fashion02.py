import tensorflow as tf
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

test_loss, test_acc = model.evaluate(test_images_refine, test_labels, verbose=2)

for idx, img in enumerate(train_images):
    cv2.imwrite("image_train/" + class_names[train_labels[idx]] + "_" + str(idx) + '.jpg', train_images[idx])

for idx, img in enumerate(test_images):
    cv2.imwrite("image_test/" + class_names[test_labels[idx]] + "_" + str(idx) + '.jpg', test_images[idx])
    
cv2.waitKey(0)
cv2.destroyAllWindows()

