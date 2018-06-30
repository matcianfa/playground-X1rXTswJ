# Première étape, on crée tous les triplets pythagoriciens et on les range par valeur de M possible
# 2 e étape on compte tous les triplets dont l'un des termes est inférieur à M

#On va supposer a priori la valeur de M max. Si besoin on augmentera. Le tout est que M_max dépasse la solution donnée à la fin
M_max=2000

# On range dans un dictionnaire qui associe à M le 2e membre du triplet. 
triplets={}

for p in range(1,max((M_max+1)//2,int((M_max/2)**0.5))+1):
    for q in range(1,p):
        x_0=x= p*p-q*q
        y_0=y= 2*p*q
        while x<=M_max or y <= M_max:
            triplets[x]=triplets.setdefault(x,set([]))|set([y])
            triplets[y]=triplets.setdefault(y,set([]))|set([x]) 
            x+=x_0
            y+=y_0 
 
# On decide que h<=l<=L pour avoir une unicité des pavés à rotation près. Dans ce cas, le plus court chemin est racine de L²+(l+h)² (Faire un dessin sur le patron du pavé). Cette longueur est un entier ssi (L,l+h) est le début d'un triplet pythagoricien.
# On remarque de plus que le nombre de chemins solutions en fonction de M est le nombre de chemins au rang M-1 + ceux pour lesquels L=M. Donc on va simplement créer la fonction nb_solutions qui donne le nb de solution lorsque L=M. Il suffira ensuite de faire la somme de 1 à M pour les avoir toutes.
def nb_solutions(M):  
    # pour un triplet (M,x) ou (x,M), on veut x=l+h, avec h<=l<=M. Pour avoir le nombre de couples qui fonctionnent, il faut donc min(M,x-1)>=l>=x/2, le h fonctionnera automatiquement. Il y a donc min(M,x-1) - x/2 + 1 solutions (ou min(M,x-1)-x/2 si x impaire).
    somme=0
    if M in triplets:
        for x in triplets[M]:
            if x//2<=M :
                if x%2 ==0:
                    somme+= min(M,x-1)-x//2+1
                else : 
                    somme+= min(M,x-1)-x//2
    return somme
    
#On calcule jusqu'à dépasser 1 million
somme=0
M=1
while somme<1000000:
    M+=1
    somme+=nb_solutions(M)
    
print(M)
