# Méthode bourrin : on prend tous les couples de points et on teste si le triangle est rectangle

from itertools import *

dimension= 50
liste_points=[point for point in product(range(dimension+1),repeat=2)]

# Fonction qui 2 points et qui vérifie si le triangle formé avec O est rectangle (en utilisant le produit scalaire)
def est_rectangle(p1,p2):
    a,b=p1
    c,d=p2
    return (a*(c-a)+b*(d-b)==0) or (a*c+b*d==0) or (c*(c-a)+d*(d-b)==0)

somme=0
for point1,point2 in combinations(liste_points[1:],2): # Ne pas oublier de retirer 0
    if est_rectangle(point1,point2):
        somme+=1
        
print(somme)
