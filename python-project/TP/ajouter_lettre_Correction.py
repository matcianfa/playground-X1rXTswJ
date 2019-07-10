def ajouter_lettre(lettre,mot_partiel,mot_choisi):
    """
    Ajoute la lettre à la bonne place dans le mot_partiel
    """
    reponse=""
    for i in range(len(mot_choisi)):
        if lettre == mot_choisi[i]:
            reponse+=lettre
        else :
            reponse+=mot_partiel[i]
    return reponse
