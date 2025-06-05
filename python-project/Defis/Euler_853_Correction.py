# ProjectEuler 853

import math
from time import time
from numba import njit
import numpy as np

def resoudre_euler_853(N,longueur):

    # Calcul des 'longueur' premiers termes de la suite de Fibonacci
    liste_fib = [1,2]
    a = 1
    b = 2
    for i in range(longueur):
        a,b = b,a+b
        liste_fib.append(b)

    print(liste_fib)

    # On cherche les n qui marchent
    reponse = 0
    fib_moins_un = liste_fib[-2]-1 # Pour que ca soit une période, il faut que le dernier soit égal à 1 modulo n ce qui permet de selectionner les n qui peuvent marcher
    fib_moins_deux = liste_fib[-1]-2
    for n in range(3,N+1):
        if fib_moins_un % n == 0 and fib_moins_deux % n == 0:
            for i in range(1,longueur//2+1) :
                if liste_fib[i]%n == 1 and liste_fib[i+1]%n == 2: # si la période est plus courte
                    break
            else :
                print(n)
                reponse += n

    return reponse


t0 = time()
sol = resoudre_euler_853(1_000_000_000,120)
print(f"La solution est {sol}")
print(f"Temps mis : {time()-t0}")
