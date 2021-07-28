from keras.datasets import mnist
import cv2

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

for i, img in enumerate(test_images):
    cv2.imwrite("test/" + str(test_labels[i]) + "_" + str(i) + '.jpg', img)
    if i > 100:
        break
    
cv2.waitKey()
cv2.destroyAllWindows()