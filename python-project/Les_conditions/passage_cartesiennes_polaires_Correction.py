from math import *

def ma_fonction(x,y):
    if y!=0 or x>0:
        r=round(sqrt(x**2+y**2),3)
        theta=round(2*atan(y/(x+r)),3)
    else :
        r=-x
        theta=round(pi,3)
    return (r,theta)
