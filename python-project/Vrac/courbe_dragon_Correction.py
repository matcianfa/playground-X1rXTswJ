def pliage(k):
    #Ne pas toucher ce qui précède
    #Les valeurs pour les variables en entrée seront automatiquement données
    #Ecrire ci-dessous en n'oubliant pas d'indenter
    while k%2==0:
        k//=2
    if k%4==1:
        return "G"
    else :
        return "D"
    
