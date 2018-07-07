# L'idée est de montrer que O est dans l'intersection des 3 demi plans en calculant les equations de (AB), (AC) et (BC) et montrer que le 3e point donne le même signe que 0 dans l'équation.

# La liste des triangles sous la forme de triplet des coordonnées des points : ((x_A,y_A),(x_B,y_B),(x_C,y_C))
liste = # A copier coller

# la fonction équation de la droite passant par (x_a,y_a) et (x_b,y_b) qui renvoit la valeur au point M
def equation(M,A,B):
    x,y=M
    x_A,y_A=A
    x_B,y_B=B
    return (y_A-y_B)*(x-x_A)+(x_B-x_A)*(y-y_A)
    
# Fonction qui cherche la solution
def chercher():
    compteur = 0
    for triangle in liste:
        for (i,j,k) in [(1,2,0),(2,1,0),(0,1,2)]: # pour regarder les 3 possibilités : droite (AC), (BC) et (AB).
            if equation(triangle[i],triangle[j],triangle[k])*equation((0,0),triangle[j],triangle[k])<0 : # Si les résultats des équations n'ont pas le même signe (et donc leur produit est negatif), on sort de la boucle
                break
        else : # Si on n'est pas sorti de la boucle c'est que O était du bon coté des 3 demi droites et donc on le compte
            compteur +=1
    return compteur
    
print(chercher())
                
