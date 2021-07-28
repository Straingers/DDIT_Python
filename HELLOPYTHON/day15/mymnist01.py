from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images[0])
print(train_labels[0])

arr2D = train_images[0]

for i in arr2D:
    for j in i:
        if j == 0:
            print(" ", end="")
        else:
            print("0", end="")
    print()

print(len(train_images))
print(len(train_labels))
print(len(test_images))
print(len(test_labels))

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, batch_size=128)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test_acc: ', test_acc)