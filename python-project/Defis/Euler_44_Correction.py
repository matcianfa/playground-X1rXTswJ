# L'idée est de considérer la somme S=P_k+P_n dans la liste des nombres pentagonaux et chercher le nombre P_n qui donnera le plus petit D=P_k-P_n=S-2*P_n encore dans la liste.
# On triche en supposant que le premier trouvé est bien le bon

#Pour gagner en vitesse, on place le tout dans une fonction
def chercher():
    # ensemble  des nombres pentagonaux qu'on remplira au fur et à mesure
    # On choisit la structure ensemble car elle va être très grande et il est beaucoup plus rapide de savoir si un element est dans un ensemble que dans une liste
    ens_penta=set([1,5])
    longueur=2  # On sauvegarde la longueur de la liste_penta pour éviter de calculer souvent avec len
    
    S=5
    
    while 1 : # Tant qu'on peut trouver un minimum en ajoutant un nouveau nombre, on continue de chercher
        for P_n in ens_penta:
            P_k= S-P_n
            D=P_k-P_n
            if P_k in ens_penta and D in ens_penta :
                return D
        longueur+=1
        S=longueur*(3*longueur-1)//2
        ens_penta.add(S) # On augmente la liste_penta d'un élément

            
print(chercher())
