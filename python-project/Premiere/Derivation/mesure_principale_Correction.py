from math import pi

def ma_fonction(angle):
    while angle > pi :
        angle -= 2*pi
    while angle <= -pi:
        angle += 2*pi
    return angle
