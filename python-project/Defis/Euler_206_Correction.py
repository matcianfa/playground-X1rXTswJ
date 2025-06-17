# ProjectEuler 206

import math
from time import time
from numba import njit
import numpy as np


# @njit("float64(int32,int32)")
def resoudre_euler_206():
    """
    Le nombre se termine par 30 ou 70
    """
    for n in range(int(10203040506070809**0.5),int(192939495969798999**0.5)):
        n2 = n**2
        if str(n2)[::2]=="123456789":
            return n*10





t0 = time()
sol = resoudre_euler_206()
print(f"La solution est {sol}")
print(f"Temps mis : {time()-t0}")
