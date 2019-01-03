from Est_premier import est_premier

def ma_fonction(a,b):
    liste_nb_premiers=[]
    for n in range(a,b+1):
        if est_premier(n):
            liste_nb_premiers.append(n)
    return liste_nb_premiers
