import cv2

img = cv2.imread("test.png", cv2.IMREAD_GRAYSCALE)

print(img)

cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

