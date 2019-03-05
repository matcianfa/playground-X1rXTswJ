import sys
import math
# Pour mémoizer :
from functools import lru_cache

rows = int(input())  # Number of rows
columns = int(input())  # Number of columns

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
    liste_bin=[int_to_bin(n) for n in liste]
    # On affiche les nombres de chaque tas en binaires
    # On affiche la sommeXor de la liste
    somme=somme_xor(liste_bin)
    # Si on est dans une situation paire, alors on joue au hasard
    if all([chiffre=="0" for chiffre in somme]):
        for k, n in enumerate(liste):
            if n>0:
                return k,1
    # Si on est dans une situation impaire, on donne le coup à jouer
    else:
        numero,valeur= rechercher_ligne_a_modifier(liste_bin,somme)
        return numero,valeur

# game loop
while True:        
    player=[]
    boss=[]
    liste=[]
    for i in range(rows):
        # x_player: Position of the first player's token
        # x_boss: Position of the second player's token
        x_player, x_boss = [int(j) for j in input().split()]
        player.append(x_player)
        boss.append(x_boss)
        liste.append(x_boss-x_player-1)

    
    row,x=jeu_nim(liste)
    print(row,x+player[row])
