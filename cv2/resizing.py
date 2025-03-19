import os 
import cv2

image_path = os.path.join('.' , 'images' , 'male1.jpeg')
image = cv2.imread(image_path)
cv2.imshow("male",image)
cv2.waitKey(5000)

resized_image = cv2.resize(image , (500,500))
cv2.imshow("resized_frame" , resized_image)
cv2.waitKey(5000)