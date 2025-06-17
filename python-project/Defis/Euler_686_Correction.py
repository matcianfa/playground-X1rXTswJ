# ProjectEuler 686

import math
from time import time
from numba import njit
import numpy as np



@njit("int64(int32)")
def resoudre_euler_686(N):

    reponse = 0
    n = 90
    compteur = 1
    log2 = math.log10(2)
    log123 = math.log10(1.23)
    log124 = math.log10(1.24)
    n_prec =0
    while compteur <N :
        n+=1
        log_a = n*log2
        if log123<= log_a - int(log_a) < log124 :
            compteur += 1
            n_prec = n

    return n



t0 = time()
sol = resoudre_euler_686(678910)
print(f"La solution est {sol}")
print(f"Temps mis : {time()-t0}")
