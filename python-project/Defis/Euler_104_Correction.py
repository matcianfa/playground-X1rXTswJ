#Methode presque directe : on cherche d'abord les nombres de fibonacci qui ont la fin pandigitale (en travaillant modulo 10**9) puis on teste si parmi ceux là, le nombre est aussi pandigital au debut (en utlisant la formule avecc le nombre d'or.

from math import log

chiffres=set([str(i) for i in range(1,10)])
# Fonction qui renvoit si un ensemble de 9 chiffres est pandigital
def est_pandigital(ens):
    return ens==chiffres
    
    
# fonction qui cherche
def chercher():
    a=b=1
    k=2
    debut=set([1])# les 9 premiers chiffres
    fin=set([1]) # Les neufs derniers
    while 1:
        a,b=b,(a+b)
        k+=1
        fin=set([chiffre for chiffre in str(b%(10**9))])
        if est_pandigital(fin) :
            debut=set([chiffre for chiffre in str(b//(10**(int(log(b,10))-8)))])
            if est_pandigital(debut):
                return k
    
    
print(chercher())
