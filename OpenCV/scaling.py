import cv2
import numpy as np

#Opening an Image file
image = cv2.imread("Small_Image.jpeg")

#Resizing image using Linear Iterpolation
linear_image =cv2.resize(image,None,fx=2.5,fy=2.5,interpolation=cv2.INTER_LINEAR )

#Resizing image using Cubic Iterpolation
cubic_image =cv2.resize(image,None,fx=2.5,fy=2.5,interpolation=cv2.INTER_CUBIC )


#Showing the images
cv2.imshow('Linear Interpolation',linear_image)

cv2.imshow('Cubic Interpolation',cubic_image)

cv2.waitKey(0)