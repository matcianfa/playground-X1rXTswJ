# ProjectEuler 141
# A optimiser : 1h de calcul

import math
from time import time
from numba import njit

@njit()
def resoudre_euler_141(N):
    solution = []
    n = 1
    while n<N :
        n_2 = n*n
        for d in range(2,n+1):
            q,r = n_2//d, n_2%d
            if q*r == d*d:
                solution.append(n)
                print(f"n={n}, d={d}, q={q}, r={r}, rapport = {d/q}")
        n+=1
    return solution



t0 = time()
sol =resoudre_euler_141(10**6)
print(sol)
print(sum([x*x for x in sol]))
print(f"Temps mis : {time()-t0}")
