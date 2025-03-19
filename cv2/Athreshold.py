import cv2 
import os

image_path = os.path.join('.' , 'images' , 'handwritten.jpeg')
image = cv2.imread(image_path)

image_gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(image_gray , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 21 , 30)

cv2.imshow("handwritten",image)
cv2.imshow("thresh" , thresh)
cv2.waitKey(10000)
