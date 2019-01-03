from math import sqrt

def ma_fonction(n):
    #J'ecarte le cas où n<2
    if n<2 : 
        return []
    else:
        #Je crée ma liste avec tous les nombres
        liste=list(range(2,n+1))
        #l'indice de parcourt de ma liste. Je commence au début.
        i=0
        while liste[i]<=sqrt(n):
            #Je retire les multiples de liste[i]
            k=2*liste[i]
            while k<=n:
                if k in liste:
                    liste.remove(k)
                k+=liste[i]
            i+=1
        return liste
