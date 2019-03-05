def est_triée(liste):
    for i in range(len(liste)-1):
        if liste[i]>liste[i+1]:
            return False
    return True
    
    
