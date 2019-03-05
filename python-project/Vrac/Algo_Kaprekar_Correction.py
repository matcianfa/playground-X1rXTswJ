def ma_fonction(n):
    n=str(n)#On va travailler avec des chaines de caractères pour pouvoir récupérer les chiffres
    longueur=len(n)
    liste_résultats=[]
    while n not in liste_résultats:
        liste_résultats.append(n)
        a=int("".join(sorted([chiffre for chiffre in n],reverse=True)))
        b=int("".join(sorted([chiffre for chiffre in n])))
        n=str(a-b)
        #On rajoute les 0 pour garder la même longueur que le chiffre du départ
        n="0"*(longueur-len(n))+n
    indice=liste_résultats.index(n)#On récupère à partir de quel indice ca boucle
    return [int(nombre) for nombre in liste_résultats[indice:]] #Attention on demande une liste d'entier et non de chaine de caractères
