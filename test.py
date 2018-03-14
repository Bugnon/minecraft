import cv2

path = "../sensehat/images/garden.png"
path2 = "/home/pi/minecraft/sensehat/images/garden.png"

image = cv2.imread(path)

cv2.imshow("Image", image)
cv2.waitKay(0)
