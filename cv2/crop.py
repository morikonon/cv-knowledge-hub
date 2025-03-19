import os 
import cv2

image_path = os.path.join('.' , "images" , 'baby1.jpeg')

image = cv2.imread(image_path)
print(image.shape)
cropped_image = image[50:150 , 100:200]

cv2.imshow("image" , image)
cv2.imshow("cropped_image" , cropped_image)
cv2.waitKey(0)