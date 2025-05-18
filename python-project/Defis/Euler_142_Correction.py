# ProjectEuler 142

import math
from time import time
from numba import njit



@njit("int64(int32)")
def resoudre_euler_142_2(N):
    somme_min =7*N*N
    for a in range(1,N):
        a2 = a*a
        for b in range(a%2+2,a,2):
            b2 = b*b
            x = (a2+b2)//2
            y = (a2 - b2)//2
            for c in range(1,a):
                c2 = c*c
                for d in range(c%2+2,c,2):
                    d2 = d*d
                    z = (c2-d2)//2
                    if 2*x!=c2+d2 or z>=y :
                        continue

                    for e in range(1,c):
                        e2 = e*e
                        for f in range(e%2+2,e,2):
                            f2=f*f
                            if  2*y== e2+f2 and 2*z ==e2-f2 and x+y+z < somme_min:
                                somme_min = x+y+z
                                print(somme_min,x,y,z)
    return somme_min


t0 = time()
sol =resoudre_euler_142_2(1000)
print(f"La solution est {sol}")
print(f"Temps mis : {time()-t0}")
