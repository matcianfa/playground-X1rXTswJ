def mon_programme(mot_clé,mot):
    mot_codé=""
    for k in range(len(mot)):
        mot_codé+=chr((ord(mot[k])-65*2+ord(mot_clé[k%len(mot_clé)]))%26+65)
    print(mot_codé)
