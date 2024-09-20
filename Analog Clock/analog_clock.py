import cv2
import numpy as np
from constants import CANVAS_SIZE, RADIUS , CENTER, COLOURS
from helper_function import get_ticks,get_hand

canvas = np.zeros(CANVAS_SIZE,dtype = np.uint8)

canvas[:] = [255,255,255]

hour_init,hour_dest,number_position =get_ticks()

# Drawing a Circle
cv2.circle(canvas,CENTER,RADIUS+20,(125,125,125),3)
 
# Creating tic lines and circles
k = 0
for i in range(len(hour_init)):
    if i % 5 == 0:
        if i % 15 == 0:
            print(f"number_position : {number_position[k]}")
            cv2.line(canvas,hour_init[i],hour_dest[i],(0,0,255),3)
            cv2.putText(canvas,f'{(k + 1) * 3}',number_position[k],cv2.FONT_HERSHEY_TRIPLEX,1.5,(0,0,0),2,cv2.LINE_AA)
            k = k + 1
        else:
            cv2.line(canvas,hour_init[i],hour_dest[i],(0,0,0),3)
    else:
        cv2.circle(canvas,hour_init[i],5,(0,0,0),-1)

while True:
    image_copy = canvas.copy()
    
    new_image = get_hand(image_copy)

    cv2.circle(image_copy,CENTER,8,(0,0,0),10)
    cv2.circle(image_copy,CENTER,7,(125,125,125),-1)

    cv2.imshow('Clock',image_copy)
    if cv2.waitKey(3) == ord('q'):
        break
    
cv2.destroyAllWindows()
