import cv2
import numpy as np

# Openning an image
image = cv2.imread("OpenCV/Small_Image.jpeg")

# Create Kernel for Filters
kernel_identity = np.array([[0,0,0],[0,1,0],[0,0,0]],dtype=np.float32)

kernel_3 = np.ones((3,3),dtype=np.float32) / 9.0 # Creating 3X3 kernel matrix

kernel_11 = np.ones((11,11),dtype=np.float32) / 121.0 # Creating 11X11 kernel matrix

# Applying filters on the image

image_identity = cv2.filter2D(image,-1,kernel_identity)

image_3 =  cv2.filter2D(image,-1,kernel_3)

image_11 =  cv2.filter2D(image,-1,kernel_11)

# Showing the filtered image
cv2.imshow("Image Identity",image_identity)
cv2.imshow("Image 3",image_3)
cv2.imshow("Image 11",image_11)

cv2.waitKey(0)