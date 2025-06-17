# ProjectEuler 800

import math
from time import time
from numba import njit
import numpy as np

@njit("int64[:](int64)")
def crible_eratosthene(n):
    if n < 2:
        return np.empty(0, dtype=np.int64)

    # Crée un tableau de booléens (True = potentiel premier)
    est_premier = np.ones(n, dtype=np.bool_)
    est_premier[0:2] = False  # 0 et 1 ne sont pas premiers

    for i in range(2, int(n**0.5) + 1):
        if est_premier[i]:
            est_premier[i*i:n:i] = False

    # Récupère les indice_as (nombres premiers)
    return np.nonzero(est_premier)[0]

n = 15704508  # C'est le nombre maximal tel que 800800^800800 < 2^n*n^2
nombres_premiers = crible_eratosthene(n)
len_nombres_premiers = len(nombres_premiers)
print(f"Nombres premiers inférieurs à {n} :", nombres_premiers)

@njit("int64(int64[:],int32)")
def resoudre_euler_800(nombres_premiers,N):
    """
    On cherche d'abord le n max tel que
    """

    M = N*math.log(N)
    a = 2
    indice_a = 0
    compteur = 0
    while 2*a*math.log(a) < M :
        log_a = math.log(a)
        for i in range(indice_a+1,len_nombres_premiers) :
            p = nombres_premiers[i]
            if p*log_a +a*math.log(p)< M:
               compteur += 1
            else : break
        indice_a += 1
        a = nombres_premiers[indice_a]
    return compteur

t0 = time()
sol = resoudre_euler_800(nombres_premiers,800800)
print(f"La solution est {sol}")
print(f"Temps mis : {time()-t0}")
