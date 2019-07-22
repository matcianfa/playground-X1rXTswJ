from math import *

def ma_fonction(BC,AC,AB):
    C = (AC**2 + AB**2 - BC**2)/(2*AB*AC)
    return acos(C)
