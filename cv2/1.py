import cv2 
import os

image = cv2.imread('photo.jpeg')

print(type(image))
print(image.shape)

second_image_path = 'images/baby1.jpeg'

image2 = cv2.imread(second_image_path)

print(image2.shape)

image_path = os.path.join('.' , 'images' , 'male1.jpeg')
image_path2 = os.path.join('.' , 'images' , 'female1.jpeg')
image_male = cv2.imread(image_path)
print(image_male.shape)

image_female = cv2.imread(image_path2)
print(image_female)

# cv2.imwrite(os.path.join('.' , 'images' , 'female1_out.jpeg') , image_female)

# cv2.imshow("image" , image_female)
# cv2.waitKey(10000)

