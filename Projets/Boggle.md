# Exemple d'IA sur le jeu Boggle

Voici un exemple complet utilisant les modules présentés dans le projet IA et jeux sur mobiles de la page précédente.

## Présentation du jeu

Le jeu consiste en une grille 4x4 de lettres. Le but est de former le plus de mots possibles  en parcourant la grille de proche en proche en se déplaçant dans les 8 directions possibles. On peut trouver ce jeu sur mobile ou facebook sous plusieurs formes (Boggle entre amis, Word Blitz).

Voici un lien vers une vidéo montrant l'algorithme en action : [Vidéo](https://youtu.be/QmHLsj6jn7s)  
On pourra remarquer que la reconnaissance des 16 caractères prend dans les 15 secondes ce qui est relativement lent et il arrive souvent qu'elle inverse les P et les D ou les I et les L(minuscule) . Donc il y a des améliorations à faire de ce coté là.

On pourra trouver les fichiers directement ici : [GitHub](https://github.com/matcianfa/archives/tree/master/Word%20Blitz)

Remarque pour pouvoir l'utiliser : il faudra recompiler les dictionnaires car ils étaient trop lourds (50 Mo). Pour cela il suffit de lancer Generer_automate.py une fois (ce qui créera un fichier en binaire nommé automate qui fait environ 56 Mo).  
Une fois que c'est fait il faut lancer le script main.py pour charger en mémoire toutes les fonctions puis pour lancer l'IA lorsque le jeu Boogle démarre, il faut taper lancer(80) pour que l'IA fasse le maximum de mots pendant 80 secondes.  
Bien sur, il faudra modifier les paramètres graphiques dans le fichier capture.py car il y a peu de chance que votre écran soit le même que le mien.

Les fichiers qui suivent étant assez bien commentés, j'espère que c'est compréhensible sans autres commentaires. Le but ici étant de montrer comment ce qui a été vu page précédente se met en place dans un projet complet.

## Récupération des données

::: capture.py
```python
"""
Script de capture et de lecture automatique des lettres
Pour que cela fonctionne il faut que les lettres soient correctement lues.
Il faudra donc surement modifier les valeurs des coordonnées de base.
Il va de soi qu'il faut selectionner une bonne fois pour toute la position de la grille de jeu (par exemple en mettant la fenetre en mode fenetre agrandie)
Pour obtenir les coordonnées, j'ai pris un screenshot de mon ecran et j'ai ouvert avec paint qui donne les coordonnées de la souris
"""


import numpy as np
from PIL import Image, ImageGrab, ImageEnhance, ImageFilter # Pour faire la capture d'ecran
#import cv2 # Pour afficher les captures d'ecran #pip install opencv-python
import pytesseract # OCR à  installer à part aussi

# Préciser le chemin à  suivre pour le fichier tesseract.exe
pytesseract.pytesseract.tesseract_cmd = 'c:\\Program Files\\Tesseract-OCR-2\\tesseract'

# 0 pour Word blitz
# 1 pour Boggle
jeu = 0

#----------------------- Constantes modifiables ( selon la position du jeu)
if jeu == 0:
    # Coordonnées de l'angle haut gauche de la première lettre (prendre un peu large mais pas trop)
    x0_lettre,y0_lettre=530,310
    # Dimension lettres
    largeur_lettre,hauteur_lettre=43,40
    # Ecart entre les lettres
    ecart_x,ecart_y=81,82
    # centre de la première lettre
    centre_lettre_x,centre_lettre_y=x0_lettre+largeur_lettre//2,y0_lettre+hauteur_lettre//2
elif jeu == 1:
    # Coordonnées de l'angle haut gauche de la première lettre (prendre un peu large mais pas trop)
    x0_lettre,y0_lettre=510,207
    # Dimension lettres
    largeur_lettre,hauteur_lettre=40,45
    # Ecart entre les lettres
    ecart_x,ecart_y=90,90
    # centre de la première lettre
    centre_lettre_x,centre_lettre_y=x0_lettre+largeur_lettre//2,y0_lettre+hauteur_lettre//2

#---------------------- Fonctions

def capturer():
    """ Capture graphiquement les lettres de la grille et renvoie la grille """
    grille=[]
    # On capture lettre à lettre
    for j in range(4):
        ligne=[]
        for i in range(4):
            # On capture la lettre de la i eme ligne et j ieme colonne
            image=ImageGrab.grab(bbox=(x0_lettre+i*ecart_x,y0_lettre+j*ecart_y,x0_lettre+i*ecart_x + largeur_lettre,y0_lettre+j*ecart_y+hauteur_lettre))

            #  Prétraitement de l'image
            image = image.convert('L')    # Echelle de gris
            #image = image.filter(ImageFilter.MinFilter())       # a little blur
            image = image.point(lambda x: 0 if x < 140 else 255) # Noir et blanc

            # Sauvegarde de l'image pour debugguer
            image.save("capture{}-{}.png".format(j,i))

            # On récupère le texte sur l'image (--psm 10 pour préciser qu'il n'y a qu'une lettre à chercher)
            text = pytesseract.image_to_string(image,config='--psm 10')
            text=text[:1] # Des fois la lecture n'est pas très bonne, on ne prend que la première lettre
            print(text)

            # Modif connues en cas de mauvaise lecture :
            if text in "|l[]" : text="I"
            # On met en majuscule car le dictionnaire est en majuscule
            text=text.upper()
            # On ajoute la lettre dans la ligne
            ligne.append(text)


        # On met la ligne complète dans la grille
        grille.append(ligne)
    return grille
```
:::

## IA

J'utilise des classes et des générateurs mais cela devrait tout de même être compréhensible.

::: IA.py
``` python
"""
L'idée de cette IA est assez simple :
On teste tous les mots valides qu'on peut créer cases après cases.
Pour gagner du temps, on génère les mots valides au fur et à mesure en créant un générateur (en utilisant yield au lieu de return)
Toujours pour gagner du temps, on n'utilise pas directement le dictionnaire pour voir si le mot existe
mais on teste au fur et à mesure si le début du mot correspond bien au début d'un mot existant.
Pour cela on modifie notre dictionnaire pour qu'il contienne tous les préfixes possibles. (Voir Generer_automate.py)
De manière pratique :
    En entrée, on reçoit la grille de lettre
    En sortie, on renvoie au fur et à mesure les mots sous forme de liste de couples (ligne,colonne)
    des cases à selectionner pour former un mot valide.


Optimisation possible : Cette IA ne prend pas en compte du tout les points de chaque lettre
(il est clair qu'il vaudrait mieux commencer la recherche par les lettres donnant le plus de points)
ni les lettres ou mots qui comptent double ou triple.
"""





class Case():
    """
    Pour gagner du temps, on crée une bonne fois pour toute les cases adjacentes de chaque case.
    """
    def __init__(self,ligne,colonne,lettre):
        self.ligne=ligne
        self.colonne=colonne
        self.lettre=lettre
        self.voisins=[]

    def distance(self,case):
        """
        Donne la distance du sup pour obtenir les cases adjacentes dans les 8 directions
        """
        return max(abs(self.ligne-case.ligne),abs(self.colonne-case.colonne))

    def __str__(self):
        """
        Pour debug : Permet d'afficher avec print les éléments intéressants d'une case (ici coordonnées et lettres)
        """
        return str((str(self.ligne),str(self.colonne),self.lettre))

def init(grille):
    """
    Transforme la grille en liste de Case
    """
    # On commence par créer nos cases
    liste=[]
    for i,ligne in enumerate(grille):
        for j,lettre in enumerate(ligne):
            liste.append(Case(i,j,lettre))

    # Maintenant, on chercher pour chaque case les voisins (ce sont ceux dont le max(abs(i-i0),abs(j-j0))==1)
    for case0 in liste:
        for case in liste:
            if case0.distance(case)==1:
                case0.voisins.append(case)

    return liste

def donner_mot(grille,dico):
    """
    Générateur qui donne le mot valide suivant dans la grille sous forme de liste des coordonnées à suivre
    """
    # On modifie la grille sous forme de liste de cases
    cases= init(grille)

    # ensemble des mots déjà trouvés pour éviter de faire plusieurs fois le même
    trouves=set([])

    # La liste des cas à regarder sous la forme (Noeud dans l'automate des mots, liste des cases du chemin déjà parcouru)
    a_explorer=[[dico.suivant(case.lettre),[case]] for case in cases]

    while a_explorer:
        noeud,chemin=a_explorer.pop()
        # En cas de mauvaise lecture dans la capture, le noeud peut etre vide. Tant pis, on continue
        if noeud is None : continue
        # Pour chaque voisin qu'on n'a pas encore utilisé, on teste si on peut faire un mot valide plus long
        for voisin in [v for v in chemin[-1].voisins if v not in chemin]:
            suivant=noeud.suivant(voisin.lettre)
            if  suivant is not None:
                a_explorer.append([suivant,chemin+[voisin]])
        if noeud.suivant(".") is not None and noeud.etiquette not in trouves : # Si on a un mot valide non encore trouvé
            trouves.add(noeud.etiquette)
            #print(noeud.etiquette)
            yield [(case.ligne,case.colonne) for case in chemin]
```
:::

## Sorties souris

Etant donné que la gestion de la souris est vraiment simple ici, j'ai mis dans le même fichier la gestion des sorties et la fonction principale qui permet de lancer le jeu. Pour de vrais projets, c'est mieux de séparer.

::: main.py
``` python
"""
Script à lancer pour jouer automatiquement à Word Blitz ou à Boggle
Il faudra surement modifier les valeurs des coordonnées des lettres dans le fichier capture.py
Un conseil : Lancer le script une première fois à vide pour charger le dictionnaire puis
ensuite lancer la fonction lancer() dans la console.
Il faut lancer dès que la grille est lisible (c'est à dire sans pertubation devant
La lecture graphique est un peu longue donc compter 10-15 sec avant le réel début de l'automatisation.
!!! IMPORTANT !!!
Comme l'ordinateur n'a pas le temps de faire tous les mots, il va continuer même quand le temps est écoulé
Pour arreter la souris, il faut aller très rapidement dans le coin haut gauche de l'écran,
ca arretera le script.
Vous pouvez aussi mettre le temps (en seconde) comme argument de lancer() pendant lequel le script va s'executer
"""

import pyautogui as ag
from time import time

import capture # Perso : Pour capturer les données à l'écran
import IA # Perso : permet de générer les réponses possibles sur la grille

import pickle #Pour sauvegarder des classes
from Generer_automate import Noeud # La classe qui a permis de faire le dictionnaire sous forme d'automate. Indispensable de l'importer pour pouvoir réouvrir sa sauvegarde

# On charge le dictionnaire (sauvegardé sous forme d'automate (cf le fichier Generer_automate.py))
# !!!! Un peu long à charger
dico=pickle.load(open('automate', 'rb')) # dico avec tous les mots

def cliquer(liste):
    """
    Fonction qui, à une liste de coordonnées dans la grille (donc entre 0 et 3),
    clique sur l'écran le long du chemin donné.
    """
    if liste:
        # On clique sur la première lettre
        i,j=liste.pop(0)
        ag.mouseDown(x=capture.centre_lettre_x+j*capture.ecart_x, y=capture.centre_lettre_y+i*capture.ecart_y)
        for i,j in liste :
            ag.moveTo(x=capture.centre_lettre_x+j*capture.ecart_x, y=capture.centre_lettre_y+i*capture.ecart_y)
        ag.mouseUp()

def lancer(temps=125):
    t0=time()
    # On récupère les données
    grille=capture.capturer()

    # On cherche dans le dictionnaire
    for mot in IA.donner_mot(grille,dico) :
        cliquer(mot)
        if time()-t0> temps : break # On s'arrete si on dépasse le temps.
```
:::
