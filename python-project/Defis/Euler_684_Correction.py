# ProjectEuler 684

import math
from time import time
from numba import njit
import numpy as np

# @njit("int64(int64)")
def S(k):
    n = k//9
    reponse =(5*(pow(10,n,1_000_000_007)-1) - 9*n)
    for i in range(k%9+1):
        reponse = (reponse + (i+1)*(pow(10,n,1_000_000_007))-1)
    return reponse

# @njit("int64()")
def resoudre_euler_684():

    reponse = 0
    a,b = 0,1
    for i in range(2,91):
        a,b = b,a+b
        print(i,b)
        reponse = (reponse + S(b))%1_000_000_007

    return reponse

t0 = time()
sol = resoudre_euler_684()
print(f"La solution est {sol}")
print(f"Temps mis : {time()-t0}")
