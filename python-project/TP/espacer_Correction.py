def espacer(mot):
    reponse = ''
    for lettre in mot:
        reponse+=lettre+' '
    return reponse[:-1] # Ne pas oublier de retirer le dernier espace
