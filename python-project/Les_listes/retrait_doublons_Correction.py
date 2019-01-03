def ma_fonction(liste):
    for element in liste:
        for i in range(liste.count(element)-1):
            liste.remove(element)
    return liste
