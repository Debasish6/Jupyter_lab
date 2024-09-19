import cv2
import datetime
import math
from constants import CANVAS_SIZE, RADIUS , CENTER, COLOURS

def get_ticks():
    hours_init = []
    hours_dest = []
    
    for i in range(0,360,6):
        x_coordinate = int(CENTER[0] + RADIUS * math.cos( i * math.pi / 180))
        y_coordinate = int(CENTER[1] + RADIUS * math.sin( i * math.pi / 180))
        hours_init.append(x_coordinate,y_coordinate)
    
    for i in range(0,360,6):
        x_coordinate = int(CENTER[0] + (RADIUS-20) * math.cos( i * math.pi / 180))
        y_coordinate = int(CENTER[1] + (RADIUS-20) * math.sin( i * math.pi / 180))
        hours_dest.append(x_coordinate,y_coordinate)
    
    return hours_init,hours_dest