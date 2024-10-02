import cv2
import numpy as np;

# Openning Image file using OpenCV
image = cv2.imread("OpenCV/Small_Image.jpeg")

# Creating Translation Matrix
matrix = np.float32([[1,0,100],[0,1,100]])

# Applying the matix to the image
euclidean_transform = cv2.warpAffine(image,matrix,(image.shape[0]+100,image.shape[1]+100))

cv2.imshow("Euclidean Image",euclidean_transform)
cv2.waitKey(0) 