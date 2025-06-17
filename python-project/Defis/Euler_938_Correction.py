# ProjectEuler 938

import math
from time import time
from numba import njit
import numpy as np


@njit("float64(int32,int32)")
def resoudre_euler_938(R,B):
    memo = np.zeros((R+1,B+1))
    memo[0,:] = 1 # Si R==0, proba = 1
    for r in range(R+1):
        memo[r,1] = 1/(r+1)

    for r in range(2,R+1,2):
        for b in range(1,B+1):
            memo[r,b]= (r*(r-1)*memo[r-2,b] + 2*r*b*memo[r,b-1])/((r+b)*(r+b-1)-b*(b-1))

    return memo[R,B]




t0 = time()
sol = resoudre_euler_938(24690,12345)
print(f"La solution est {round(sol,10)}")
print(f"Temps mis : {time()-t0}")

