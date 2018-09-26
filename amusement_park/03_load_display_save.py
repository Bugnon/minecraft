import cv2

path = "../sensehat/images/garden.png"

image = cv2.imread(path)

cv2.imshow("Image", image)
cv2.waitKey(0)