# L'idée est de créer un graphe de relation sous forme de dictionnaire puis le parcourir.
# Le plus simple est d'en faire 2 : Un qui regroupe pour un chiffre donné ceux qui suivent et un qui regroupe les antécédents possibles. En jouant avec les deux, on devrait réussir à reconstruire le nombre 
# On admet que chaque chiffre n'apparait qu'une fois au plus !

# Liste des codes partiels rentrés : 
liste= ['319', '680', '180', '690', '129', '620', '762', '689', '762', '318', '368', '710', '720', '710', '629', '168', '160', '689', '716', '731', '736', '729', '316', '729', '729', '710', '769', '290', '719', '680', '318', '389', '162', '289', '162', '718', '729', '319', '790', '680', '890', '362', '319', '760', '316', '729', '380', '319', '728', '716']

#Dictionnaires dans lesquels on range les successeurs et les antécédents de chaque chiffre
succ={}
anté={}

for code in liste : 
    for i in range(2): #la flemme de copier 2 fois :)
        succ[code[i]]=succ.setdefault(code[i],set([]))|set([code[i+1]]) # On utilise des ensembles pour que les doublons s'éliminent automatiquement
        anté[code[i+1]]=anté.setdefault(code[i+1],set([]))|set([code[i]])
        anté[code[i]]=anté.setdefault(code[i],set([])) # Uniquement la pour créer les nombres sans antécédents
     

#Maintenant que notre graphe est construit, on commence par le chiffre qui n'a pas d'antécédent. Ensuite on élimine ce chiffre des antécédents de tous ses succésseurs. Puis on passe à celui qui n'a plus d'antécédents etc.
réponse = ""
while 1 :
    liste_sans_anté=sorted([chiffre for chiffre,ens in anté.items() if not ens])
    chiffre=liste_sans_anté[0] # Si il y en a plusieurs, on prend le plus petit même si le programme est fait en admettant qu'on est sur de trouver une combinaison valide en faisant ainsi (ce qui n'est pas évident)
    réponse+= chiffre # On ajoute le chiffre à la réponse
    # maintenant on retire ce chiffre des antécédents de ses successeurs :)
    if chiffre in succ: # S'il n'y a plus de successeurs, c'est que c'est fini. C'est là où sert l'hyothèse qu'on va trouver la solution facilement c'est à dire qu'on a suffisamment de données pour ne pas avoir plusieurs réponses possibles. Sinon il aurait fallu les chercher toutes voire même vérifier la cohérence avec le graphe de départ...
        for successeur in succ[chiffre]:
            anté[successeur].discard(chiffre)
        del anté[chiffre] # On le supprime pour ne plus l'obtenir quand on cherche les chiffres sans antécédents
    else : break
    
print(réponse)        
        
