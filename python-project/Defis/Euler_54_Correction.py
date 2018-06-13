''' 
L'idée générale de cette solution est la suivante : 
On transforme chaque main en ne s'interessant dans un premier temps qu'aux valeurs qu'on regroupe. Par exemple une main avec 2 paires "3C 5D 6C 5C 3D" donnera ([2,2,1][5,3,6]). 
La premiere liste correspond aux nombres de cartes des valeurs qui se trouvent dans la deuxième liste (ici il y a deux 5, deux 3 et un 6).
L'astuce est que pour comparer deux mains, il suffit de comparer ces groupes. En effet une main qui donne [3,1,1] gagne une main [2,2,1] qui elle même gagne [2,1,1]. Et en cas d'égalité la comparaison se fait automatiquement sur la liste des valeurs. On utilise donc l'ordre sur les listes déjà existant en python.
Il faut cependant considérer à part les suites et les couleurs en les transformant à la main en liste qui se comparent comme il faut. Par exemple la suite bat le brelan mais est moins qu'un full. il suffit donc de lui associer une liste comprise entre [3,1,1] et [3,2]. On peut choisir [3,1,2] par exemple et pour la couleur [3,1,3].
'''

parties= ''' à copier coller'''

#On transforme en liste chaque partie
liste_parties=[ligne.split() for ligne in parties.split("\n")[1:-1]]

# dictionnaire pour transformer les cartes en valeur numérique (valet = 11,... , As=14)
valeurs = {"T":10, "J" : 11, "Q" : 12, "K":13, "A":14}
for i in range(2,10):
    valeurs[str(i)]=i
    
# fonction qui transforme une main (c'est à dire la liste ['9C', 'JD', '7C', '6D', 'TC']) en deux listes contenant d'un coté les valeurs et de l'autre les couleurs : ([9,11,7,6,10],[C,D,C,D,C])
def transformer_main(main):
    liste_valeurs=[]
    liste_couleurs=[]
    for carte in main:
        liste_valeurs.append(valeurs[carte[0]])
        liste_couleurs.append(carte[1])
    return (liste_valeurs,liste_couleurs)
    
# fonction qui transforme une liste de valeurs [3,5,6,5,3] en couple donnant le nombre de valeurs et les valeurs dans l'ordre décroissant ensuite (ici ([2,2,1],[5,3,6]) car il y a deux 5, deux 3 et un 6)
def transformer_valeurs(valeurs):
    # On crée un dico qui compte puis on le renversera pour chaque valeur le nombre d'occurence
    dic={}
    for valeur in valeurs:
        dic[valeur]=dic.setdefault(valeur,0)+1
    #On crée une petite liste avec le couple (nombre d'occurence,valeur) pour la trier
    liste_temp=[(nb,val) for (val,nb) in dic.items()]
    liste_temp.sort(reverse=True)
    #Enfin on les regroupe comme on veut
    liste_nb=[]
    liste_val=[]
    for (nb,val) in liste_temp:
        liste_nb.append(nb)
        liste_val.append(val)
    return (liste_nb,liste_val)
    

# Fonction globale qui va transformer une main directement en couple de liste comme on veut en tenant compte cette fois des couleurs et des suites    
def transformer(main):
    valeurs,couleurs=transformer_main(main)
    liste_nb,liste_val=transformer_valeurs(valeurs)
    if liste_nb==[1,1,1,1,1]: # Les couleurs et suites ne peuvent se produire que dans le cas où toutes les valeurs sont distinctes
        couleur,suite=False,False #Un booléen pour mémoriser si on a une couleur ou une suite pour éviter la répétition de tests
        if len(set(couleurs))==1 : # on transforme la liste en ensemble. S'il n'y a qu'un élément c'est qu'il n'y a qu'une seule couleur et donc on a une couleur
            couleur=True
        if max(liste_val)-min(liste_val)==4 : # Si la différence des valeurs max - min vaut 4 (on sous entend qu'il n'y a que des cartes distinctes) alors on a forcément une suite.
            suite=True
        #affectons à présent les valeurs qu'il faut à liste_nb dans le cas des couleurs et des suites
        if couleur and suite : #Quinte flush doit battre le carré donc on va lui associer [5] ou [4,2]
            liste_nb=[5]
        elif couleur: # Pour la couleur simple on a déjà éxpliqué précédemment qu'on lui associerait [3,1,3] pour être entre la couleur et le full
            liste_nb=[3,1,3]
        elif suite: # De même, on a dit qu'on lui associerait [3,1,2] pour être entre le brelan et la suite
            liste_nb=[3,1,2]
    return liste_nb,liste_val

# Il ne reste plus qu'à comparer toutes les parties :
compteur=0
for partie in liste_parties:
    #print(partie,transformer(partie[:5]),transformer(partie[5:]))
    if transformer(partie[:5])>transformer(partie[5:]):
        #print("J1")
        compteur+=1
print(compteur)
