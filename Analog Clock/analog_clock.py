import cv2
import numpy as np
from constants import CANVAS_SIZE, RADIUS , CENTER, COLOURS
from helper_function import get_ticks

canvas = np.zeros(CANVAS_SIZE,dtype = np.uint8)

canvas[:] = [255,255,255]

hour_init,hour_dest =get_ticks()

# Drawing a Circle
cv2.circle(canvas,CENTER,RADIUS+20,(125,125,125),3)
 
# Creating tic lines and circles

for i in range(len(hour_init)):
    if i % 5 == 0:
        if i % 15 == 0:
            cv2.line(canvas,hour_init[i],hour_dest[i],(0,0,255),3)
        else:
            cv2.line(canvas,hour_init[i],hour_dest[i],(0,0,0),3)
    else:
        cv2.circle(canvas,hour_init[i],5,(0,0,0),-1)

cv2.imshow('Clock',canvas)
cv2.waitKey(0)
