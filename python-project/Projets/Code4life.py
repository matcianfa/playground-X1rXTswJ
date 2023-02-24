import sys
from collections import namedtuple

# ----------- Fonctions Auxiliaires

def log(*x):
    """
    Permet d'afficher des données utiles comme un message d'erreur (et donc qui ne sera pas considéré comme une réponse)
    Ex : log(a,b,c) affichera les valeurs de a, b et c
    """
    print(*x, file=sys.stderr, flush = True)

def donner_nombre_molecules_manquantes(robot,fichier):
    """
    Fonction permettant de savoir le nombre de molécules qu'il nous manque pour chaque sort de molécules
    """
    molecules_manquantes = []
    for i in range(5):
        if fichier.couts[i] > robot.molecules[i] :
            molecules_manquantes.append(fichier.couts[i] - robot.molecules[i])
        else :
            molecules_manquantes.append(0)
    return molecules_manquantes

# ----------- Constantes et variables

MOI = 0
ADV = 1
CLOUD = -1

ABCDE = "ABCDE"

Fichier = namedtuple('Fichier', [
    'id', 'porteur', 'rang', 'vie', 'couts', 'gain_expertise'
    ])

Robot = namedtuple('Robot',[
    'position','temps_arrivee','score','molecules','expertise'
    ])


liste_projets = []
mes_fichiers = []
ses_fichiers = []
fichiers_stockés = []





nombre_projets = int(input())
for i in range(nombre_projets):
    liste_projets.append([int(j) for j in input().split()])

# ------------ Boucle du jeu
while True:

    # -------- Récupération des données pour ce tour de jeu

    robots = []
    for i in range(2):
        inputs = input().split()
        position = inputs[0]
        inputs = [int(i) for i in inputs[1:]]
        robots.append(Robot(position,*inputs[:2],inputs[2:7],inputs[7:]))

    mon_robot, son_robot = robots

    molecules_dispo = [int(i) for i in input().split()]
    nombre_fichiers = int(input())
    mes_fichiers = []
    ses_fichiers = []
    fichiers_stockés = []
    for i in range(nombre_fichiers):
        inputs = input().split()
        gain_expertise = inputs.pop(3)
        inputs = [int(i) for i in inputs]
        fichier = Fichier(*inputs[:4],inputs[4:],gain_expertise)
        
        if fichier.porteur == MOI :
            mes_fichiers.append(fichier)
        elif fichier.porteur == ADV :
            ses_fichiers.append(fichier)
        else :
            fichiers_stockés.append(fichier)
    

    # ------------------------------------------
    # ------------- Logique du jeu -------------
    # ------------------------------------------

    if mon_robot.temps_arrivee > 0 :                                    # Si on est en déplacement
        print("WAIT")

    elif len(mes_fichiers) == 0 and mon_robot.position != "DIAGNOSIS":  # Si on n'a pas de fichiers dans les mains (A modifier pour la ligue Bois 1 )
        print("GOTO DIAGNOSIS")

        
    # ------- Gestion du module SAMPLES (A partir de la ligue bois 1)

    elif mon_robot.position == "SAMPLES" :
        print("WAIT")

    # ------- Gestion du module DIAGNOSIS

    elif mon_robot.position == "DIAGNOSIS" :                             
        if len(mes_fichiers) < 1 :
            fichier_choisi = fichiers_stockés[0]
            print(f"CONNECT {fichier_choisi.id}")
        
        else :
            print("GOTO MOLECULES")

    # ------- Gestion du module MOLECULES

    elif mon_robot.position == "MOLECULES" :
        molecule_necessaire = -1
        for fichier in mes_fichiers :
            molecules_manquantes = donner_nombre_molecules_manquantes(mon_robot, fichier)
            for i in range(5) :
                if molecules_manquantes[i] > 0 :
                    molecule_necessaire = i
                    break
        
        if molecule_necessaire == -1 :          # Si on n'a pas trouvé de molécules manquantes
            print("GOTO LABORATORY")
        else :
            print(f"CONNECT {ABCDE[molecule_necessaire]}")

    # ------- Gestion du module LABORATORY

    elif mon_robot.position == "LABORATORY" :
        print("WAIT")
