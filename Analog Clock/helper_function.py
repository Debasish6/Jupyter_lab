import cv2
from datetime import datetime
import math
from constants import CANVAS_SIZE, RADIUS , CENTER, COLOURS

def get_ticks():
    hours_init = []
    hours_dest = []
    number_position =[]
    
    for i in range(0,360,6):
        x_coordinate = int(CENTER[0] + RADIUS * math.cos( i * math.pi / 180))
        y_coordinate = int(CENTER[1] + RADIUS * math.sin( i * math.pi / 180))
        hours_init.append((x_coordinate,y_coordinate))
    
    for i in range(0,360,6):
        x_coordinate = int(CENTER[0] + (RADIUS-20) * math.cos( i * math.pi / 180))
        y_coordinate = int(CENTER[1] + (RADIUS-20) * math.sin( i * math.pi / 180))
        hours_dest.append((x_coordinate,y_coordinate))
    
    for i in range(0,360,90):
        x_coordinate = int(CENTER[0] - 15 + (RADIUS-50) * math.cos( i * math.pi / 180))
        y_coordinate = int(CENTER[1] + 15 + (RADIUS-50) * math.sin( i * math.pi / 180))
        number_position.append((x_coordinate,y_coordinate))
    
    return hours_init,hours_dest,number_position

def get_hand(image):
    timenow = datetime.now()
    hour = math.fmod(timenow.hour, 12)
    minute = timenow.minute
    second = timenow.second
    
    second_angle = math.fmod(second * 6 + 270 , 360)
    minute_angle = math.fmod(minute * 6 + 270 , 360)
    hour_angle = math.fmod((hour * 30) + (minute / 2) + 270 , 360)
    
    # Drawing Second hand
    x_second = int(CENTER[0] + (RADIUS-50) * math.cos( second_angle * math.pi / 180))
    y_second = int(CENTER[1] + (RADIUS-50) * math.sin( second_angle * math.pi / 180))
    cv2.line(image,CENTER,(x_second,y_second),(0,0,0),2)
    
    # Drawing Minute hand
    x_minute = int(CENTER[0] + (RADIUS-30) * math.cos( minute_angle * math.pi / 180))
    y_minute = int(CENTER[1] + (RADIUS-30) * math.sin( minute_angle * math.pi / 180))
    cv2.line(image,CENTER,(x_minute,y_minute),(0,0,0),5)
    
    # Drawing Hour hand
    x_hour = int(CENTER[0] + (RADIUS-100) * math.cos( hour_angle * math.pi / 180))
    y_hour = int(CENTER[1] + (RADIUS-100) * math.sin( hour_angle * math.pi / 180))
    cv2.line(image,CENTER,(x_hour,y_hour),(0,0,0),8)
    
    return image
    
    