import sys
from collections import namedtuple
from random import randint

# -------------- Fonctions auxiliaires

def log(*x):
    print(*x, file=sys.stderr, flush=True)


# -------------- CONSTANTES

MON_ROBOT = 0
SON_ROBOT = 1
RADAR = 2
PIEGE = 3
CRISTAL = 4
VIDE = -1

LARGEUR, HAUTEUR = [int(i) for i in input().split()]

# -------------- Variables utilisées

cristaux = None             # Liste contenant les cristaux visibles
mes_robots = None           # Liste contenant mes robots
ses_robots = None           # Liste contenant les robots de l'adversaire
radars = None               # Liste contenant mes radars
pieges = None               # Liste contenant mes pieges

# -------------- Classes

# Un Objet permettra de stocker les données d'un robot, d'un radar ou d'un piège.
Objet = namedtuple('Objet',['id','type','x','y','objet'])

# un Cristal permet de stocker les coordonnées et quantité d'un gisement de cristal
Cristal = namedtuple('Cristal',['x','y','quantite'])

# -------------- Commandes pour les robots

def aller_a(x,y) :  print(f"MOVE {x} {y}")

def creuser(x,y) :  print(f"DIG {x} {y}")

def attendre() :    print("WAIT")

def prendre_radar() : print("REQUEST RADAR")

def prendre_piege() : print("REQUEST TRAP")

# -------------- Boucle du jeu
while True:
    # ---------- Initialisation
    cristaux = []
    mes_robots = []
    ses_robots = []
    radars = []
    pieges = []
    objets = [mes_robots, ses_robots, radars, pieges]

    # ---------- Récupération des données
    mon_score, son_score = [int(i) for i in input().split()]

    # --- Mise à jour des données des cristaux
    for ligne in range(HAUTEUR):
        inputs = input().split()
        for colonne in range(LARGEUR):
            quantite_cristal = inputs[2*colonne]
            trou = int(inputs[2*colonne+1]) # Non géré par ce kit de démarrage
            cristaux.append(Cristal(colonne,ligne,quantite_cristal))


    nombre_objets, radar_cooldown, trap_cooldown = [int(i) for i in input().split()]

    # --- Mise à jour et rangement des Objets (robots, radars et pieges)
    for i in range(nombre_objets):
        objet = Objet(*[int(j) for j in input().split()])
        objets[objet.type].append(objet)
        

    # ------------------------------------------
    # ------------- Logique du jeu -------------
    # ------------------------------------------


    for n_robot in range(5):
        robot = mes_robots[n_robot]

        if robot.objet == CRISTAL : # Si on a un cristal, ...
            attendre()
        else :                      # Sinon on choisit un endroit où creuser au hasard
            x = randint(1,LARGEUR-1)
            y = randint(0,HAUTEUR-1)

            creuser(x,y)

