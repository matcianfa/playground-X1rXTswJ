from math import pi
from fractions import Fraction

def ma_fonction(angle):
    angle/=pi
    while angle > 1 :
        angle -= 2
    while angle <= -1:
        angle += 2
    return "("+str(Fraction(angle).limit_denominator())+')pi'
