# L'idée de ce programme est de voir les opérations comme un arbre ou les noeuds sont des opérations et les feuilles sont des nombres. Du coup il y a 3 structures pour l'arbre : soit 3 noeuds d'affilés à gauche, soit à droite soit symétrique.

from itertools import permutations,combinations

# Les opérations
def addition(a,b):
    return a+b
    
def soustraction(a,b):
    return a-b
    
def multiplication(a,b):
    return a*b
    
def division(a,b):
    return a/b

operations=[addition,soustraction,multiplication,division]

# Fonction qui calcule en prenant en argument les valeurs des nombres 
def calcul(nombres):
    reponses=set([])
    for a,b,c,d in permutations(nombres):
        for op1 in operations:
            for op2 in operations:
                for op3 in operations:
                    #arbre gauche
                    try :
                        reponse = op1(op2(op3(a,b),c),d)
                        if reponse>0 and round(reponse,3)==int(reponse):
                            reponses.add(int(reponse))
                    except : pass
                    #arbre droit
                    try : 
                        reponse = op1(a,op2(b,op3(c,d)))
                        if reponse>0 and round(reponse,3)==int(reponse):
                            reponses.add(int(reponse))
                    except : pass
                    #arbre symétrique
                    try : 
                        reponse = op1(op2(a,b),op3(c,d))
                        if reponse>0 and round(reponse,3)==int(reponse):
                            reponses.add(int(reponse))
                    except : pass
    return reponses
    
# Fonction qui à une liste renvoie la plus grande valeur d'entier consécutifs en partant de 1
def long_chaine(liste):
    liste=sorted(liste)
    for i,n in enumerate(liste):
        if i+1!=n:
            return i
                     
                     
# Enfin la fonction qui cherche
def chercher():
    long_max=0
    liste_max=[]
    for nombres in combinations(list(range(1,10)),4):
        temp = long_chaine(list(calcul(nombres)))
        if temp > long_max:
            liste_max=nombres
            long_max=temp
    return "".join([str(c) for c in liste_max])
    
print(chercher())
            
