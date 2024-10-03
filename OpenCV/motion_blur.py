import cv2
import numpy as np

# Opening an image
image = cv2.imread("OpenCV/Small_Image.jpeg")

# Create Kernel for Filters
size = 15
kernel = np.zeros((15,15))

kernel[int((size-1)/2),:] = np.ones(size)

kernel = kernel / size

# Applying filters on the image

image_motion = cv2.filter2D(image,-1,kernel)


# Showing the filtered image
cv2.imshow("Image Motion",image_motion)
cv2.imshow("Image",image)

cv2.waitKey(0)