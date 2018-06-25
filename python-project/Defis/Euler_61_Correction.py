#L'idée est de créer un dictionnaire pour chaque type de nombre polygonal où on met en clé les 2 premiers chiffres et en valeur la liste des deux derniers chiffres possibles associés aux deux premiers chiffres

from itertools import permutations

liste_dic=[]

# Fonction P(k,n)
def P(k,n):
    if k==3: return n*(n+1)//2
    if k==4: return n*n
    if k==5: return n*(3*n-1)//2
    if k==6: return n*(2*n-1)
    if k==7: return n*(5*n-3)//2
    if k==8: return n*(3*n-2)
    
#Création des dictionnaires
for k in range(3,9):
    dic={}
    n=1
    p=1
    while p<10000:
        if p>1000 :
            p=str(p)
            dic[p[:2]]=dic.setdefault(p[:2],[])+[p[2:]]
        n+=1
        p=P(k,n)
    liste_dic.append(dic)
    
somme_min=10**10
# Comme on cherche le premier qui marche, on le fait avec une fonction
# k designe l'indice où on en est dans notre cycle et chemin garde en mémoire le chemin suivi
def chercher(liste_permutations,precedent='',chemin=[]):
    global somme_min
    if len(chemin)==7:
        if chemin[0]==chemin[-1]:# Si c'est bien un cycle on calcule la somme 
            somme=0
            for i in chemin[:-1] : 
                somme+=int(i)*101 # Astuce : Si on reprend l'exemple de l'énoncé : pour ajouter les 3 nombres 8128+2882+8281 on peut ajouter 8100+28+2800+82+8200+81 ce qui revient à additionner 81*101+28*101+82*101
            if somme<somme_min :
                somme_min=somme
    elif len(liste_permutations)==6 :
        for debut in liste_dic[liste_permutations[0]-3]:
            for fin in liste_dic[liste_permutations[0]-3][debut]:
                chercher(liste_permutations[1:], fin, [debut,fin])
    else :
        for fin in liste_dic[liste_permutations[0]-3].setdefault(precedent,[]):
            chercher(liste_permutations[1:],fin, chemin+[fin])
            
for liste_permutations in permutations(range(3,9)):
    chercher(liste_permutations)
            
print(somme_min)
