def ma_fonction(mot_clé,mot):
    mot_codé=""
    for k in range(len(mot)):
        mot_codé+=chr((ord(mot[k])-65*2+ord(mot_clé[k%len(mot_clé)]))%26+65)
    return mot_codé
