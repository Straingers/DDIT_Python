import cv2

img = cv2.imread('shose.jpg',  cv2.IMREAD_GRAYSCALE)
img_28 = cv2.resize(255 - img, dsize=(28, 28))
cv2.imshow('Test Image', img)
img_28_refine = img_28 / 255.0
img_28_refine = img_28_refine.reshape(1, 28, 28)

print(img_28_refine.reshape)
print(img_28_refine)

cv2.waitKey(0)
cv2.destroyAllWindows()