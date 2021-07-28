from tensorflow.keras import datasets
import cv2
 
cifar10 = datasets.cifar10 
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
 
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
 
train_images_refine = train_images.reshape((50000, 32, 32, 3))
test_images_refine = test_images.reshape((10000, 32, 32, 3))

train_images_refine = train_images / 255.0
test_images_refine = test_images / 255.0
 
for idx, img in enumerate(train_images):
    if idx == 100:
        break
    cv2.imwrite("cifar_train/" + str(train_labels[idx][0]) + "_" + str(idx) + '.jpg', train_images[idx])

for idx, img in enumerate(test_images):
    if idx == 100:
        break
    cv2.imwrite("cifar_test/" + str(test_labels[idx][0]) + "_" + str(idx) + '.jpg', test_images[idx])
cv2.waitKey(0)
cv2.destroyAllWindows()
 