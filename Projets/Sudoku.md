# Exemple d'IA sur la résolution d'un sudoku

Voici un autre exemple complet utilisant les modules présentés dans le projet IA et jeux sur mobiles de la page précédente.

## Présentation

Je ne présente pas le sudoku qui est un classique et dont les règles se trouvent facilement par ailleurs. 
Comme pour les autres projets, on utilise un jeu de sudoku déjà existant, notre but est de récupérer graphiquement les données et les interpréter (avec Tesseract) puis de d'utiliser une IA qui résout la grille. Voici [une vidéo](https://youtu.be/XksFVThUmWA) du résultat en utilisant une application android (sur émulateur donc) qui donne des grilles de Sudoku (d'où les pubs qu'on peut voir...). 

## Récupération des données

Comme pour Boogle, on utilise tesseract pour traduire l'image en chiffre ici. 

::: capture.py
``` python
"""
Fonction de capture graphique de la grille. On fait une capture d'ecran case par case et on le dechiffre avec Tesseract
"""


import numpy as np
from PIL import Image, ImageGrab, ImageEnhance, ImageFilter # Pour faire la capture d'ecran
import cv2 # Pour afficher les captures d'ecran #pip install opencv-python
import pytesseract # OCR à  installer à part aussi

# Préciser le chemin à  suivre pour le fichier tesseract.exe
pytesseract.pytesseract.tesseract_cmd = 'c:\\Program Files\\Tesseract-OCR-2\\tesseract'





#---------------------- Fonctions

def capturer(x0,y0,x1,y1):
    """ Capture graphiquement les nombres de la grille et renvoie la grille """

    dim_case_x,dim_case_y=(x1-x0)//9,(y1-y0)//9
    grille=[]
    print("Lecture de la grille:")
    print("+---+---+---+")
    for i in range(9):
        ligne=[]
        print("|",end="")
        for j in range(9):

            # On capture le chiffre de la i eme ligne et j ieme colonne
            image=ImageGrab.grab(bbox=(x0+j*dim_case_x,y0+i*dim_case_y,x0+(j+1)*dim_case_x,y0+(i+1)*dim_case_y))

            #  Prétraitement de l'image
            image = image.convert('L')    # Echelle de gris
            image = image.filter(ImageFilter.MinFilter())       # a little blur
            image = image.point(lambda x: 0 if x <80 else 255) # Noir et blanc avec seuil bas pour faire disparaitre la grille

            # Sauvegarde de l'image pour debugguer
            image.save("capture{}-{}.png".format(j,i))

            # On récupère le texte sur l'image
            text = pytesseract.image_to_string(image,config='--psm 10')
            if text=="": text="0"
            print(text,end="")
            if j%3==2 : print("|",end="")
            ligne.append(int(text))
        print("")
        if i%3==2: print("+---+---+---+")
        grille.append(ligne)
    return grille



if __name__ == '__main__':
    pass
    print(capturer(500,133,857,491))
```
:::

## IA

L'algorithme est un classique qui peut servir assez souvent : un backtracking.

::: IA.py
``` python
"""
Script de résolution d'une grille de Sudoku
Prend en entrée un grille de sudoku classique (pas numpy) et donne en sortie la grille remplie.
On utilise un algorithme de retour sur trace (backtracking)
"""


#-------------------- Fonctions auxilliaires

def ajout_possible_sur_ligne(grille,i,valeur):
    """
    Vérifie si la valeur existe déjà sur la i eme ligne
    """
    for j in range(9):
        if grille[i][j]==valeur: return False
    return True

def ajout_possible_sur_colonne(grille,j,valeur):
    """
    Vérifie si la valeur existe déjà sur la i eme ligne
    """
    for i in range(9):
        if grille[i][j]==valeur: return False
    return True

def ajout_possible_dans_bloc(grille,i,j,valeur):
    """
    Vérifie si la valeur existe déjà sur la i eme ligne
    """
    i0,j0=i//3,j//3
    for di in range(3):
        for dj in range(3):
            if grille[i0*3+di][j0*3+dj]==valeur: return False
    return True

def suivant(i,j):
    """
    Donne la case suivante pour parcourir la grille comme on la lirait
    """
    if j<8: return (i,j+1)
    return (i+1,0)


#-------------------- Fonction principale

def donner_solution(grille):
    """
    Fonction qui résoud le sudoku et renvoie la solution
    """
    # On copie la grille
    reponse=[ligne.copy() for ligne in grille]

    def backtracking(grille,i,j):
        """
        On cherche case par case les valeurs possibles.
        Dès qu'une case ne peut pas être remplie, on revient en arriere pour tester une autre valeur
        """
        global reponse
        if i==9 :# Si on a parcouru toute la grille c'est qu'on a réussi à la remplir
            reponse=[ligne.copy() for ligne in grille]
            return True
        if grille[i][j]!=0 :
            return backtracking(grille,*suivant(i,j)) # Si la case est déjà remplie, on passe à la suivante
        # On teste toute les valeurs possibles pour une case
        for valeur in range(1,10):
            # Si la valeur n'est pas encore dans la ligne, colonne ou bloc
            if ajout_possible_sur_ligne(grille,i,valeur) and ajout_possible_sur_colonne(grille,j,valeur) and ajout_possible_dans_bloc(grille,i,j,valeur):
                # On remplit la grille avec cette valeur
                grille[i][j]=valeur
                if backtracking(grille,*suivant(i,j)):
                    return True
                # On retire la valeur de la grille puisque si on en est ici du programme c'est qu'on n'a pas réussi à finir la grille
                grille[i][j]=0
        # Si on en est là c'est qu'on n'a pas réussi à trouver une valeur qui convient
        return False

    # On lance la recherche de solution en partant de la première case
    backtracking(reponse,0,0)

    return reponse



if __name__=="__main__": # Pour le debug
    grille=[[0, 1, 0, 0, 0, 0, 4, 3, 0], [7, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 5, 4, 9, 0, 0], [1, 7, 0, 0, 4, 0, 2, 0, 6], [0, 0, 0, 0, 9, 0, 0, 0, 3], [0, 0, 3, 0, 0, 6, 0, 8, 0], [0, 0, 1, 4, 7, 0, 0, 6, 0], [0, 0, 0, 5, 0, 8, 1, 2, 0], [0, 9, 0, 0, 6, 0, 3, 0, 4]]
    #grille=[[0, 0, 0, 8, 0, 5, 0, 1, 3], [0, 0, 0, 2, 0, 3, 6, 0, 0], [6, 0, 0, 0, 9, 0, 2, 0, 4], [0, 0, 0, 0, 0, 0, 0, 0, 5], [0, 4, 0, 1, 0, 0, 7, 0, 6], [2, 5, 6, 3, 0, 4, 8, 9, 0], [5, 9, 0, 0, 0, 7, 1, 0, 2], [1, 0, 2, 0, 8, 0, 4, 7, 0], [0, 0, 4, 9, 1, 0, 0, 3, 8]]
    print(donner_solution(grille))
```
:::

## Sorties souris

Rien de particulier, on clique sur la case puis on clique sur le chiffre qu'on veut y mettre.

::: main.py
``` python
"""
Script principal pour résoudre graphiquement des sudokus
On s'est basé sur un jeu de Sudoku sur un emulateur Android (Memu Play) nommé simplement Sudoku.
Pour jouer, il faut cliquer sur la case puis cliquer sur le numéro que l'on souhaite mettre dans cette case en dessous de la grille
"""
import pyautogui as ag # Permet la gestion de la souris
import capture # Perso : Pour capturer les données à l'écran
import IA # Perso : permet de générer les réponses possibles sur la grille
import time

#----------------------- Constantes modifiables ( selon la position du jeu)
x0,y0,x1,y1=500,133,857,491
dim_case_x,dim_case_y=(x1-x0)//9,(y1-y0)//9

# Liste donnant les positions des cases sur lesquelles il faut cliquer pour rentrer la valeur
positions_x_chiffres=[None,523,562,601,639,678,717,757,796,835]
positions_y_chiffres=628

def cliquer(i,j,valeur):
    """
    Fonction qui rentre la valeur dans la case se trouvant à la ligne i et colonne j
    """
    # On selectionne la case à remplir
    ag.click(x0+j*dim_case_x + dim_case_x//2,y0+i*dim_case_y+dim_case_y//2)

    # On clique sur la valeur
    ag.click(positions_x_chiffres[valeur],positions_y_chiffres)


def lancer():
    t0=time.time()
    # On récupère les données
    grille=capture.capturer(x0,y0,x1,y1)
    t1=time.time()
    print("Capture effectuée en {} s".format(round(t1-t0,1)))
    print("Recherche de la solution")
    # On détermine la solution
    solution = IA.donner_solution(grille)
    print("Solution trouvée en {} s".format(round(time.time()-t1,1)))
    # On remplit la grille sur l'emulateur
    for i in range(9):
        for j in range(9):
            if grille[i][j]==0: # Si la case etait vide au début, on la remplit
                cliquer(i,j,solution[i][j])
```
:::





