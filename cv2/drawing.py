import cv2 
import os

image_path = os.path.join('.', 'images', 'whiteboard.jpeg')

image = cv2.imread(image_path)

if image is None:
    print("Ошибка при загрузке изображения. Проверьте путь.")
    exit()

image = cv2.resize(image, (720, 420))

cv2.rectangle(image, (200, 200), (400, 400), (255, 0, 0), 3)  # Синий прямоугольник

cv2.circle(image, (350, 450), 15, (255, 0, 255), 5)  # Розовый круг

cv2.putText(image, "Hello", (600, 450), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 10)  

cv2.imshow("whiteboard", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
