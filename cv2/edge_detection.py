import cv2
import os
import numpy as np

image_path = os.path.join('.' , 'images' , 'messi.jpeg')

image = cv2.imread(image_path)
image = cv2.resize(image , (720 , 420))

image_edge_detection = cv2.Canny(image , 50,200)

image_edge_detection_d = cv2.dilate(image_edge_detection , np.ones((3,3) , dtype = np.int8))
image_edge_detection_e = cv2.erode(image_edge_detection , np.ones((3,3) , dtype = np.int8))

cv2.imshow("messi",image) 
cv2.imshow("messi_edge_detection" , image_edge_detection)
cv2.imshow("messi_d" , image_edge_detection_d)
cv2.imshow("messi_e" , image_edge_detection_e)
cv2.waitKey(10000)