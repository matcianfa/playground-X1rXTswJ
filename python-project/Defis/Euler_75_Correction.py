# On va utiliser la caractérisation des triplets pythagoriciens primitifs. Donc pour p,q premier entre eux et de parité différente, q<p :
# x = p²-q²
# y = 2pq
# z = p²+q²
# Du coup L=x+y+z = 2p(p+q). Donc il suffit de chercher pour des valeurs de p<=racine(L/2)

L_max=1500000

# Dictionnaire dans lequel on va associé à chaque valeur de L l'ensemble des triplets associés
dic={}

# Fonction qui à p,q renvoit le triplet pythagoricien associé (rangé dans l'ordre
def triplet(p,q):
    return sorted((p*p-q*q,2*p*q,p*p+q*q))
    
# Fonction qui insère le triplet t dans le dictionnaire
def insérer(t):
    global dic
    s=sum(t)
    dic[s]=dic.setdefault(s,set([]))|set([t])

# On cherche dans une fonction pour aller plus vite
def chercher():
    for p in range(1,int((L_max/2)**0.5)+1):
        for q in [q for q in range(1,p) if (p+q)%2==1]:
            t=triplet(p,q)
            L= sum(t)
            if L< L_max : 
                for k in range(1,L_max//L+1): # On regarde les multiples des triplets primitifs
                    insérer(tuple([k*x for x in t]))
    compteur=0
    for L in dic: # On cherche ceux avec 1 seul triplet
        if len(dic[L])==1 : 
            compteur += 1
    return compteur
    
print(chercher())
