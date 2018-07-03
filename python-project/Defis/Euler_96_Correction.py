# l'idée est de résoudre les sudoku en entier par backtracking puis de récupérer les 3 premiers chiffres

liste_grilles= # A copier coller


# Vérifications que le chiffre qu'on veut rajouter n'est pas déjà...
# Sur la ligne
def vérif_ligne(valeur, ligne, grille):
    for col in range(9):
        if grille[ligne][col]==valeur : return False
    return True
    
# Sur la colonne
def vérif_colonne(valeur, col,grille):
    for ligne in range(9):
        if grille[ligne][col]==valeur : return False
    return True
    
# Dans un bloc
def vérif_bloc(valeur, ligne, col,grille):
    l0=ligne-ligne%3 #Pour avoir la ligne supérieure du bloc
    c0=col -col%3 # idem pour la colonne
    for l in range(3):
        for c in range(3):
            if grille[l0+l][c0+c]==valeur: return False
    return True
    
# Fonction qui résout notre sudoku par backtracking 
# La position est celle quand on numérote les cases de 1 à 81 pour augmenter facilement de 1
def résoudre(grille, position=0):
    global grille_temp
    if position==81 : # On a tout rempli
        return True
    ligne = position//9
    col = position%9
    if grille[ligne][col]!=0 : # Si la grille a déjà un numéro 
        return résoudre(grille,position+1)
    for chiffre in range(1,10):
        if vérif_ligne(chiffre, ligne,grille) and vérif_colonne(chiffre,col,grille ) and vérif_bloc(chiffre, ligne,col,grille) : # Si chiffre n'est ni sur la ligne la colonne ou le bloc alors on le teste
            grille[ligne][col]=chiffre
            if résoudre(grille,position+1):
                return True
    # On réinitialise si ca n'a pas marché
    grille[ligne][col]=0
    return False

   
# Il n'y a plus qu'à récolter la somme des nombres formés des 3 premiers chiffres
somme=0
for grille in liste_grilles:
    résoudre(grille)
    somme+= grille[0][0]*100 + grille[0][1]*10+grille[0][2] 
    
print(somme)

        
