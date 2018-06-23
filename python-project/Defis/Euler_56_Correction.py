# Méthode bourrin : On teste tous les cas vu que Python sait gérer les très grands nombres.

# Fonction qui donne la somme des chiffres d'un nombre.
def sommer_chiffres(n):
    str_n=str(n)
    somme=0
    for chiffre in str_n:
        somme+=int(chiffre)
    return somme
    
somme_max=0
for a in range(100):
    n=1
    for b in range(100):
        somme_chiffres=sommer_chiffres(n)
        if somme_chiffres>somme_max:
            somme_max=somme_chiffres
        n*=a #Pour éviter de recalculer à chaque fois a^b, on multiplie simplement le résultat précédent par a

print(somme_max)
