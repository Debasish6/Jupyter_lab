import cv2
import numpy as np

#Opening an Image file
image = cv2.imread("Small_Image.jpeg")

#Translation Matrix
matrix = np.float32([[1,0,100],[0,1,100]])

# Applying matrix to the image(Here I use warpAffine function)
translated_image = cv2.warpAffine(image, matrix ,(image.shape[1]+100, image.shape[0]+100))

# Showing the result
cv2.imshow('Translated Image',translated_image)
cv2.waitKey(0)
 