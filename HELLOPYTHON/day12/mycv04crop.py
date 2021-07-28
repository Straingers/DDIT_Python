import cv2

img = cv2.imread('iu.jpg',  cv2.IMREAD_COLOR)
img_crop = img[300:650, 500:750]
print(len(img))
print(len(img[0]))

cv2.imshow('Test Image', img_crop )
cv2.imwrite('iu_face.jpg', img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()