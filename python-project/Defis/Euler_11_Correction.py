maximum=0

# On cherche d'abord le maximum selon les lignes
for i in range(20):
    for j in range(17):
        produit = grille[i][j]*grille[i][j+1]*grille[i][j+2]*grille[i][j+3]
        if produit > maximum:
            maximum = produit

# On cherche maintenant le maximum selon les colonnes
for i in range(17):
    for j in range(20):
        produit = grille[i][j]*grille[i+1][j]*grille[i+2][j]*grille[i+3][j]
        if produit > maximum:
            maximum = produit

# On cherche finalement le maximum selon les diagonales dans un sens
for i in range(17):
    for j in range(17):
        produit = grille[i][j]*grille[i+1][j+1]*grille[i+2][j+2]*grille[i+3][j+3]
        if produit > maximum:
            maximum = produit

# On cherche finalement le maximum selon les diagonales dans l'autre sens
for i in range(3,20):
    for j in range(17):
        produit = grille[i][j]*grille[i-1][j+1]*grille[i-2][j+2]*grille[i-3][j+3]
        if produit > maximum:
            maximum = produit

print(maximum)
