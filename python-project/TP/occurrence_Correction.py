def compter(lettre,texte):
    compteur = 0
    for L in texte.lower() :
        if L == lettre :
            compteur += 1
    return compteur
