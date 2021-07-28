import cv2

img = cv2.imread('iu_face.jpg')

height, width = img.shape[:2]

M = cv2.getRotationMatrix2D((width/2.0, height/2.0), -10, 1)
img_rotation = cv2.warpAffine(img, M, (width, height))

cv2.imshow("Test Image", img_rotation)
cv2.waitKey(0)
cv2.destroyAllWindows()