# ProjectEuler 932

import math
from time import time
from numba import njit



#@njit("int64(int32)")
def resoudre_euler_932(N):
    reponse = 81
    for nb_chiffres_b in range(1,N//2+1):
        puiss_dix_b = 10**nb_chiffres_b
        for b in range(puiss_dix_b//10,puiss_dix_b):
            delta = puiss_dix_b*(puiss_dix_b-4*b)+4*b
            if delta > 0 :
                sqrt_delta = math.isqrt(delta)
                if sqrt_delta**2 == delta:
                    for a in range(max(1,puiss_dix_b//100),b):
                        if a*puiss_dix_b + b ==(a+b)**2 :
                            print(a*puiss_dix_b + b,a,b,(b*(b-1))//a)
                            reponse += (a+(b*(b-1))//a)*puiss_dix_b + 2*b
    return reponse



t0 = time()
sol =resoudre_euler_932(16)
print(f"La solution est {sol}")
print(f"Temps mis : {time()-t0}")
