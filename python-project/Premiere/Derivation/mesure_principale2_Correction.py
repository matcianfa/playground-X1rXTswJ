from math import pi

def ma_fonction(angle):
    angle/=pi
    while angle > 1 :
        angle -= 2
    while angle <= -1:
        angle += 2
    return str(angle)+'pi'
