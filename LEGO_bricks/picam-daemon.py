import threading
import os, io, base64, time, socket, picamera, daemon
import daemon.runner



MAX_LENGTH = 50 # max length of any possible entry from "client"
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # setup socket
PORT = 10000 # port 10000
HOST = '127.0.0.1' # runs on local host
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # this allows us to override port, prevents error
serversocket.bind((HOST, PORT)) # lock server to this port and host
serversocket.listen(1) # max 10 clients

# Runs over "sockets"
def handle(clientsocket):
	while 1:
		buf = clientsocket.recv(MAX_LENGTH)
		
		# Receive the SNAP command. Take a picture with PiCam.
		if buf == ‘pic’:
			start = time.time()
			camera.capture(‘new_picture.jpg’)
			finish = start - time.time()
			print finish
			print 'Picture Taken!'
		
		if len(buf) == 0: break

# Camera is always loaded here
# The "magic" is in the camThread, this allows a picture to be captured, then it gracefully closed the camera connection and reopens it. This produces very fast captures (54ms vs 1.5s!)
while 1:
	# setup camera
	camera = picamera.PiCamera()
	camera.resolution = (640, 480)
	#camera.zoom = (0.2, 0.2, 1.0, 1.0)
	camera.exposure_mode = 'sports'
	print('Camera server running')
	  
	# accept connections from outside, in order to receive commands
	(clientsocket, address) = serversocket.accept()
	ct = threading.Thread(target=handle, args=(clientsocket,))
	ct.run() # this can be run(), because it can be scaled.
	
	print 'Camera thread starting.'
	camThread = threading.Thread()
	while camThread.is_alive():
		camThread.join(1)
	camThread.run() # this must be start(), otherwise PiCam will crash. This is because PiCam cannot receive more than 1 connection.
	print 'Camera thread ended'
	camera.close() # Gracefully close PiCam if client disconnects