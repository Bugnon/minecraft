# import the necessary packages

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

GREEN = (0, 255, 0)

class FaceDetector:
	def __init__(self, faceCascadePath):
		# load the face detector
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

	def detect(self, image, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30)):
		# detect faces in the image
		rects = self.faceCascade.detectMultiScale(image,
			scaleFactor = scaleFactor, minNeighbors = minNeighbors,
			minSize = minSize, flags = cv2.CASCADE_SCALE_IMAGE)

		# return the rectangles representing boundinb
		# boxes around the faces
		return rects


# initialize the camera and grab a reference to the raw camera
# capture
camera = PiCamera()
#camera.resolution = (640, 480)
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))

# construct the face detector and allow the camera to warm
# up
fd = FaceDetector("cascades/haarcascade_frontalface_default.xml")
time.sleep(0.1)

t0 = time.time()
# capture frames from the camera
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image
    frame = f.array

    t1 = time.time()
    print(t1-t0)
    t0 = t1
    
    # resize the frame and convert it to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the image and then clone the frame
    # so that we can draw on it
    faceRects = fd.detect(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))
    frameClone = frame.copy()

    # loop over the face bounding boxes and draw them
    for (x, y, w, h) in faceRects:
        cv2.rectangle(frameClone, (x, y), (x + w, y + h), GREEN, 2)

    # show our detected faces, then clear the frame in
    # preparation for the next frame
    cv2.imshow("Face", frameClone)
    rawCapture.truncate(0)

    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break