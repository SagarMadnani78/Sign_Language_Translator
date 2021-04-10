import cv2

image = cv2.imread('bird.jpg',0)

cv2.imwrite('birdBW.png',image)

cv2.imshow('Converted to GrayScale',image)

cv2.waitKey(0)

cv2.destroyAllWindows()
