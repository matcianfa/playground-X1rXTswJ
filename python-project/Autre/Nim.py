# Pour mémoizer :
from functools import lru_cache

#--------------- Outils---------------
@lru_cache(maxsize=None)
def int_to_bin(n):
    """
    Transforme un entier sous forme binaire 
    entrée -> int 
    sortie -> chaine de caractères
    """
    if n<2 : return str(n)
    return int_to_bin(n//2)+str(n%2)
    
@lru_cache(maxsize=None)
def bin_to_int(b):
    """
    Transforme une chaine de caractère en binaire en un entier
    """
    if len(b)==1: return int(b)
    return bin_to_int(b[:-1])*2+int(b[-1]) 
    
    
def xor(a,b):
    """ 
    transforme deux nombres en ecriture binaire en leur somme XOR (c'est à dire sans retenue) sous forme binaire aussi
    Entrée et sortie sous forme de chaine de caractères
    """
    if a=="" : return b
    if b=="" : return a
    return xor(a[:-1],b[:-1])+str((int(a[-1])+int(b[-1]))%2)
    
def somme_xor(liste):
    """ 
    renvoie la somme des éléments de la liste en utilisant le xor comme addition
    """
    if len(liste)==0 : return 0
    if len(liste)==1 : return liste[0]
    return xor(liste[0],somme_xor(liste[1:]))
    
def rechercher_ligne_a_modifier(liste,somme):
    """
    On sait qu'il existe un indice i tel que xor(somme_xor(liste),liste[i]) < liste[i]. Ici on le cherche.
    Sortie : l'indice de la ligne ainsi que la valeur à retirer en valeur entière
    """
    for k,c in enumerate(liste):
        int_xor= bin_to_int(xor(somme,c))
        int_c= bin_to_int(c)
        if int_xor<int_c :
            return (k,int_c-int_xor)
    print("Pas trouvé de ligne à modifier")
    return(-1,-1)
    
def espacer(texte):
    """
    rajoute un espace entre chaque caractère
    """
    reponse=""
    for lettre in texte:
        reponse+=" "+lettre
    return reponse
    
#------------------ Le jeu --------------

def jeu_nim(liste):
    """
    Cette fonction a simplement pour but de donner la liste contenant le nombre d'allumettes de chaque tas et renvoyer les décompositions en base 2 ainsi que la somme Xor suivi du coup à jouer pour se ramener à un cas pair
    """
    print("Décomposition en base 2 de chaque tas :\n")
    liste_bin=[int_to_bin(n) for n in liste]
    longueur_max=max([len(c) for c in liste_bin])
    # On affiche les nombres de chaque tas en binaires
    for k,c in enumerate(liste_bin):
        print("Tas n°{} : {}".format(k,"  "*(longueur_max-len(c))+espacer(c)))
    # On affiche la sommeXor de la liste
    somme=somme_xor(liste_bin)
    print("-"*(10+2*longueur_max))
    print("Parité  : {}".format(espacer(somme)))
    print("\n")
    # Si on est dans une situation paire, alors on joue au hasard
    if all([chiffre=="0" for chiffre in somme]):
        print("On est dans une situation paire : Jouer au hasard")
    # Si on est dans une situation impaire, on donne le coup à jouer
    else:
        numero,valeur= rechercher_ligne_a_modifier(liste_bin,somme)
        print("Pour gagner, il faut retirer {} allumette(s) du tas n°{}".format(valeur,numero))
        
