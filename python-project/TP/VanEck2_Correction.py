def VanEck(n):
    liste_termes = [0]

    # liste_indices[k] = l'indice le plus grand tel que k apparait dans la liste_termes
    # On crée de suite une liste remplie de None de taille n+1 (même si la fin de la liste a de forte chance de ne servir à  rien)
    liste_indices = [None]*(n+1)
    for indice in range(n):
        # Le terme qu'on considère
        v_n = liste_termes[-1]
        # On rajoute dans la liste le nombre indice-liste_indices[indice] qui correspond au nombre de fois où il faut reculer pour retrouver le mÃªme
        # Sauf dans le cas où liste_indices[indice]==0 qui signifie qu'on n'a toujours pas trouvé cette valeur
        if liste_indices[v_n] is None :
            liste_termes.append(0)
        else :
            liste_termes.append(indice-liste_indices[v_n])
        # On met à  jour la liste_indices car la dernière occurence du dernier terme est désormais indice
        liste_indices[v_n] = indice
    return liste_termes
