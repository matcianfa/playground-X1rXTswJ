"""
Euler 135
On ecrit x,y,z sous la forme d+r,d,d-r. On obtient que n est forcément de la forme d(4r-d).
Donc il suffit de chercher les nombres n tels que l'ensemble des diviseurs tels que n//d est divisible par 4 (pour pouvoir trouver r)
et d>r (pour que z soit positif) ait une taille de 10.
"""

from sympy import divisors
  

def chercher(N,nb_solutions):
    compteur = 0
    for n in range(1,N):
        if len([d for d in divisors(n,generator = True) if (d+n//d)%4==0 and (n//d+d)//4<d]) == nb_solutions:
            compteur+=1
            print("\r",n,end="")
    return compteur
        
            

print("\n",chercher(1000000,10))
