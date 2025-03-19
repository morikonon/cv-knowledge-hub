import os
import cv2

image_path = os.path.join('.' , 'images'  , 'beer1.jpeg')

image = cv2.imread(image_path)
image = cv2.resize(image , (720,420))

gray_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

ret , thresh = cv2.threshold(gray_image , 80 , 255 , cv2.THRESH_BINARY)

blur_thresh = cv2.blur(thresh , (10,10))
cv2.imshow("beer" , image)
cv2.imshow("gray_beer" , gray_image)
cv2.imshow("thresh_beer" , thresh)
cv2.imshow("thresh_blur_beer" , blur_thresh)

cv2.waitKey(10000)