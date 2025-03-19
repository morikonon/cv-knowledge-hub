import cv2
import os

image_path = os.path.join('.' , 'images' , 'bird1.jpeg')

image = cv2.imread(image_path)
resized_image = cv2.resize(image , (720,420))

img_gray = cv2.cvtColor(resized_image , cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(resized_image , cv2.COLOR_BGR2HSV)

cv2.imshow("gray_img",img_gray)
cv2.imshow("hsv_image" , img_hsv)
cv2.imshow("resized_image" , resized_image)
cv2.waitKey(10000)