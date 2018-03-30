# On remarque que le problème revient à trouver deux restes dans la division euclidienne des puissances de 10 par d identiques
maximum=0
d_max=0
for d in range(1,1000):
    liste_restes=[]
    puissance_de_dix=10
    reste=0
    while reste not in liste_restes :
        liste_restes.append(reste)
        reste=puissance_de_dix%d
        puissance_de_dix*=10
    longueur=len(liste_restes)-liste_restes.index(reste)
    if reste!=0 and maximum<longueur:
        maximum=longueur
        d_max=d

print(d_max)
