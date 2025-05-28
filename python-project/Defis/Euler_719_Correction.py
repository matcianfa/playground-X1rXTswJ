# ProjectEuler 719

import math
from time import time
# from numba import njit

def est_S(n,n_2,somme=0):
    # print(n,n_2,somme)
    if somme>n or n_2<=0 : return False
    if somme + n_2 == n : return True
    nb_chiffres = int(math.log10(n_2))+1
    for k in range(1,nb_chiffres):
        mod = 10**k
        if est_S(n,n_2//mod,somme+(n_2%mod)):
            return True
    return False


#@njit("int64(int32)")
def resoudre_euler_719(N):
    reponse = 81 # on commence à 10
    for n in range(10,10**N+1):
            n_2 = n*n
            if est_S(n,n_2):
                # print(n_2)
                reponse += n_2
    return reponse



t0 = time()
sol =resoudre_euler_719(6)
print(f"La solution est {sol}")
print(f"Temps mis : {time()-t0}")
