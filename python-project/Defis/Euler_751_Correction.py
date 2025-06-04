# ProjectEuler 751

import math
from time import time
from numba import njit
from decimal import Decimal, getcontext # Pour modifier la précision des décimales

getcontext().prec = 25

def tau(theta):
    b = theta
    reponse = str(int(b))+"."
    while len(reponse)<25:
        b = int(b)*(b-int(b)+1)
        reponse += str(int(b))
    return reponse

def dist(theta):
    return theta- Decimal(tau(theta))

# @njit("int64(int32)")
def resoudre_euler_751():
    a=Decimal('2')
    b=Decimal('3')
    d_a = dist(a)
    d_b = dist(b)
    while 1:
        m = (a+b)/2
        d_m = dist(m)
        print(d_m,a,b,m)
        if abs(d_m) < Decimal('0.000000000000000000000001'):
            return m
        elif d_m*d_a >0 :
            d_a = d_m
            a = m
        else :
            d_b = d_m
            b = m


t0 = time()
sol =resoudre_euler_751()
print(f"La solution est {round(sol,24)}")
print(f"Temps mis : {time()-t0}")
