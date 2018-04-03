from decimal import *
getcontext().prec=4000

def modifier_précision(f):
    return lambda n:Decimal(f(n))
