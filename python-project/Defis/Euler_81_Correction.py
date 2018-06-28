# L'idée est de partir de l'angle inférieur droit et de remonter selon l'anti diagonale en ajoutant à chaque fois le min du nombre en dessous et à droite.

from math import inf

matrice= # A copier coller

N=len(matrice)

# On modifie un peu notre matrice pour rajouter des infinis a droite et en dessous pour éviter des disjonctions de cas
for ligne in matrice :
    ligne.append(inf)
matrice.append([inf]*(N-1)+[0,0]) # On rajoute 0 en dessous de l'angle en bas à droite pour que si on ajoute le min d'en dessous et d'à droite l'angle ne soit pas modifié

for s in range(2*N-2,-1,-1): # On parcourt l'anti diagonale telle que indice ligne+indice colonne = s
    for ligne in range(N):
        colonne = s-ligne
        if colonne in range(N): # On ne considère que les indices qui sont dans notre matrice
            matrice[ligne][colonne]+= min(matrice[ligne+1][colonne], matrice[ligne][colonne+1])
            
print(matrice[0][0])
            
