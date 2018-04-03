# Ne pas modifier
# Ceci permet de définir la précision des calculs à 4000 chiffres après la virgule.
from decimal import *
getcontext().prec=4000

def modifier_précision(f):
    return lambda n:Decimal(f(n))
