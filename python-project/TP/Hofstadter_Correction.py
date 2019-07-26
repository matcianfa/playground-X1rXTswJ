def Q(n):
    liste = [0,1,1] # On met 0 en indice 0 juste pour décaler pour que les indices soient corrects ( pour que Q(1)=liste[1] ...)
    for i in range(3,n+1):
        liste.append(liste[i-liste[i-1]]+liste[i-liste[i-2]])
    return liste[1:]
