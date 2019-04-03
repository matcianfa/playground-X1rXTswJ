from math import *

def ma_fonction(t,n):
    if n==0:
        return round(1.8*t+32,3)
    else:
        return round((t-32)/1.8,3)
