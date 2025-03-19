import cv2 
import os

image_path = os.path.join('.' , 'images' , 'freelancer1.jpeg')

image = cv2.imread(image_path)
image = cv2.resize(image , (720,420))

k_size = 100
blurred_image = cv2.blur(image , (k_size , k_size))

cv2.imshow("freelancer" , image)
cv2.imshow("blurred_freelancer" , blurred_image)
cv2.waitKey(10000)