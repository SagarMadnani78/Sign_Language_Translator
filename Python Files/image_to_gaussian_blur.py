import cv2

image = cv2.imread('bird.jpg',0)

matrix = (9,11)

image_blur = cv2.GaussianBlur(image,matrix,0)

cv2.imshow('Smoothened Image',image_blur)

cv2.waitKey(0)

cv2.destroyAllWindows()
