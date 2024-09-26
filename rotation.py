import cv2
import numpy as np

#Opening an Image file
image = cv2.imread("Small_Image.jpeg")

height, width = image.shape[:2]

matrix = cv2.getRotationMatrix2D((width/2,height/2),10,1)

rotated_image = cv2.warpAffine(image, matrix, (width,height))

cv2.imshow("Roteted Image",rotated_image)
cv2.waitKey(0)