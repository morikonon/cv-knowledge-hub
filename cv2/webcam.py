import cv2
import os

#read webacm

video_from_webcam = cv2.VideoCapture(0)

# visualize webcam

while True:
	ret , frame = video_from_webcam.read()

	cv2.imshow("frame" , frame)

	if cv2.waitKey(40) & 0xFF == ord('q'):
		break
video_from_webcam.release()
cv2.destroyAllWindows()