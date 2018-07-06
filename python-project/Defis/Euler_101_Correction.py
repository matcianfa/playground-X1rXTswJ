# L'idée est d'utiliser les polynomes de Lagrange

# fonction qui prend en entrée une liste et une fonction et crée la fonction polynôme de Lagrange de cette fonction pour cette liste de valeur 
def Lagrange(liste,f):
    # On crée la fonction de lagrange associée à un indice particulier
    def L(x,n_k):
        num=f(n_k)
        den=1
        for n in liste:
            if n!=n_k :
                num*=(x-n)
                den*=(n_k-n)
        return num/den
    # La fonction de lagrange associée à la liste et f
    def Lag(x):
        somme=0
        for n_k in liste:
            somme+=L(x,n_k)
        return somme
    return Lag
    
# Fonction qu'on veut extrapoler. On a modifier l'écriture pour minimiser les calculs
def f(x):
    return 1-x*(1-x*(1-x*(1-x*(1-x*(1-x*(1-x*(1-x*(1-x*(1-x)))))))))
    
#Fonction qui cherche
def chercher():
    reponse=0
    liste = list(range(1,20)) # On prend de la marge
    for k in range(10):
        L=Lagrange(liste[:k+1],f)
        BOP=k+1
        while L(BOP)==f(BOP):
            BOP+=1
        reponse+=L(BOP)
    return reponse
    
print(int(chercher()))
    
