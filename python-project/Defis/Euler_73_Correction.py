# L'idée est de trouver pour chaque d, le nombre de n compris entre d//3+1 et d//2.
# et de sommer au fur et a mesure en enlevant les fractions qu'on peut réduire (en regardant le nombre de n non premiers avec d entre  d//3 et d//2

# Euclide 
def pgcd(m,n): 
    while m%n: 
        r=m%n 
        m=n 
        n=r 
    return n 
    
# Fonction qui donne le nombre de n non premier avec d entre a et b
def non_premier(d,a,b):
    compteur=0
    for n in range(a+1,b+1):
        if pgcd(n,d)!=1 :
            compteur+=1
    return compteur


somme=0
for d in range(4,12001):
    a=d//3
    b=d//2
    if d%2==0 : somme += b -a-1-non_premier(d,a,b-1)
    else : somme+= b-a-non_premier(d,a,b)
        
print(somme)
