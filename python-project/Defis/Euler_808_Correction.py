# ProjectEuler 808

import math
from time import time
from numba import njit


def generateur_premier():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

@njit
def est_premier(n):
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# @njit("int64(int32)")
def resoudre_euler_808(N):
    reponse = 0
    compteur = 0
    gen_premier = generateur_premier()
    while compteur < N :
        str_p2 = str(next(gen_premier)**2)
        str_inv_p2 = str_p2[::-1]
        inv_p2 = int(str_inv_p2)
        sqrt_inv_p2 = math.isqrt(inv_p2)
        if str_p2!= str_inv_p2 and sqrt_inv_p2**2 == inv_p2 and est_premier(sqrt_inv_p2):
            compteur += 1
            reponse += int(str_p2)
            print(compteur,str_p2)

    return reponse


t0 = time()
sol =resoudre_euler_808(50)
print(f"La solution est {sol}")
print(f"Temps mis : {time()-t0}")
