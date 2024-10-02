import cv2
import numpy as np;

# Openning Image file using OpenCV
image = cv2.imread("OpenCV/Small_Image.jpeg")
rows,cols =image.shape[:2]

# Defining Source point and Destination Point
src_points = np.float32([[0,0],[cols-1,0],[0,rows-1]])
des_points = np.float32([[0,0],[int(0.6*(cols-1)),0],[int(0.4* (cols-1)),rows-1]])

# Creating Translation Matrix
affine_matrix = cv2.getAffineTransform(src_points,des_points)

# Applying the matix to the image
Affine_transform = cv2.warpAffine(image,affine_matrix,(cols,rows))

cv2.imshow("Euclidean Image",Affine_transform)
cv2.waitKey(0) 