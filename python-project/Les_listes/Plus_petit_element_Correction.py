def ma_fonction(liste):
    minimum=liste[0]
    liste_indices=[]
    for indice, element in enumerate(liste):
        if element<minimum:
            minimum=element
            liste_indices=[indice]
        elif element==minimum:
            liste_indices.append(indice)
    return liste_indices
