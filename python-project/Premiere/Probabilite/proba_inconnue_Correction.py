from mes_fonctions import lancer

def ma_fonction():
    nb_essais = 1000000
    resultats = [0,0,0]
    for i in range(nb_essais):
        n = lancer()
        resultats[n-1] += 1
    return [ n/nb_essais for n in resultats ] # On divise par le nombre d'essais pour obtenir la fréquence


