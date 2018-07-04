# L'astuce pour gagner enormément de temps est de ne pas chercher tous les anagrammes mais plutot de parcourir la liste des mots, ranger les lettres dans l'ordre alphabétique et du coup les anagrammes auront les mêmes lettres une fois ordonnées. Il ne reste plus qu'a compter les doublons...
# Deuxième point : pour ne pas chercher toutes les combinaisons possibles de chiffres associés à une lettre, on parcourt la liste des carrés et on teste si on peut associer à chaque lettre d'une anagramme les chiffres de ce carré ce qui nous donne une table de traduction. On prend une autre anagramme qu'on traduit et on vérifie si c'est de nouveau un carré.

# La liste des mots
liste_mots= # A copier coller


# Une petite recherche préalable nous donne :
# La longueur maximum des mots est 14.
# La première paire d'anagramme est de longueur 9 donc ca ne sert à rien de chercher des carrés ayant plus de chiffres.


# print(max([len(mot) for mot in liste_mots]))

#fonction qui donne l'ensemble des carrés d'entiers ayant k chiffres
def donner_carrés(k):
    return set([str(n*n) for n in range(int(10**((k-1)*0.5)),int(10**(k*0.5))+1)])

# Fonction qui renvoie un dictionnaire ayant comme valeur les anagrammes d'un même mot.
# Crée deux dictionnaires : un qui range les lettres des mots dans l'ordre pour compter les anagrammes et l'autre qui sauvegarde les mots d'origine. On s'intéresse qu'au mots de longueur k (pour descendre la valeur de k au besoin)
def chercher_anagrammes(k):
    dic_comptes={}
    dic_ana={}
    for mot in [mot for mot in liste_mots if len(mot)==k]:
        mot_ord=tuple(sorted(mot))
        dic_comptes[mot_ord]=dic_comptes.setdefault(mot_ord,0)+1
        dic_ana[mot_ord]=dic_ana.setdefault(mot_ord,[])+[mot]
    for mot,val in dic_comptes.items():
        if val==1:
            del dic_ana[mot]
    return dic_ana
    
# Fonction qui renvoie le carré maximum qu'on puisse obtenir pour une liste d'anagrammes anas parmi la liste des carrés
def chercher_carrés(anas,carrés):
    mot=anas.pop()
    reponse=""
    for carré in carrés:
        trad={}
        utilisées=set([])
        ok=True
        #On crée un dictionnaire de correspondance chiffre lettre
        for lettre,chiffre in zip(mot,carré):
            try :
                if (chiffre not in trad and lettre not in utilisées) or trad[chiffre]==lettre : 
                    trad[chiffre]=lettre
                    utilisées.add(lettre)
                else : 
                    ok=False
            except KeyError : # Au cas ou la lettre est utilisée mais pas associée au chiffre
                ok= False
        if ok:
            for ana in anas :
                #On traduit les anagrammes en chiffres pour voir si ce sont des carrés
                for chiffre,lettre in trad.items():
                    ana=ana.replace(lettre,chiffre)
                if ana in carrés : 
                    reponse=max(ana,carré, reponse)
    return reponse
                    
# Fonction qui cherche la solution
def chercher():
    reponse=""
    for k in range(14,0,-1): #On cherche le plus grand donc on parcourt du plus grand au plus petit
        for _,anas in chercher_anagrammes(k).items():
            reponse=max(reponse,chercher_carrés(anas,donner_carrés(k)))
        if reponse:
            return reponse
            
print(chercher())
    
                
