# ProjectEuler 816

import math
from time import time
from numba import njit
import numpy as np

limite_methode = 11714782

@njit("int64(int32)")
def resoudre_euler_816(N):
    reponse = 10**12

    # On génère les points
    liste_points = []
    s0 = 290797
    for i in range(N):
        s1 = (s0*s0)%50515093
        liste_points.append((s0,s1))
        s0 = (s1*s1)%50515093

    # Recherche des points les plus proches
    liste_points.sort()
    for i in range(N-1):
        (x0,y0) = liste_points[i]
        for j in range(i+1,N):
            (x1,y1) = liste_points[j]
            if (x0-x1)**2 + (y0-y1)**2 < reponse:
                reponse = (x0-x1)**2 + (y0-y1)**2
            elif (x0-x1)**2 > reponse :
                break

    return reponse


t0 = time()
sol =resoudre_euler_816(2000000)
print(f"La solution est {round(sol**0.5,9)}")
print(f"Temps mis : {time()-t0}")
