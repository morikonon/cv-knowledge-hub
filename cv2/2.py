import cv2
import os

#read video

video_path = os.path.join('.' , 'videos' , 'mountain1.mp4')

video = cv2.VideoCapture(video_path)

# visualize video

ret = True
image_frames = []
while ret:
	ret , frame = video.read()
	image_frames.append(frame)
	if ret:
		cv2.imshow("frame" , frame)
		cv2.waitKey(1)
video.release()
cv2.destroyAllWindows()