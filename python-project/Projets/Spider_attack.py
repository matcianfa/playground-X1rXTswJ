import sys
from collections import namedtuple

# ----------- Fonctions Auxiliaires

def log(*x):
    """
    Permet d'afficher des données utiles comme un message d'erreur (et donc qui ne sera pas considéré comme une réponse)
    Ex : log(a,b,c) affichera les valeurs de a, b et c
    """
    print(*x, file=sys.stderr, flush = True)

def attendre():
    """
    Pour donner l'instruction d'attendre
    """
    print("WAIT")

def aller_a(x,y):
    """
    Pour donner l'instruction de se déplacer vers le point de coordonnées (x,y)
    """
    print(f"MOVE {x} {y}")

def aller_vers_cible(cible):
    """
    Pour donner l'instruction de se déplacer vers l'Agent cible (qui peut être un monstre ou un héros)
    """
    print(f"MOVE {cible.x} {cible.y}")

def lancer_bouclier(cible):
    """
    Pour donner l'instruction de lancer le sort SHIELD sur l'Agent cible (qui doit être un monstre ou un héros)
    """
    print(f"SPELL SHIELD {cible.id}")

def lancer_vent(direction_x,direction_y):
    """
    Pour donner l'instruction de lancer le sort WIND dans la direction du point de coordonnées (x,y)
    """
    print(f"SPELL WIND {direction_x} {direction_y}")

def lancer_controle(cible,x,y):
    """
    Pour donner l'instruction de lancer le sort CONTROL sur l'Agent cible et lui indiquer de se diriger vers le point de coordonnées (x,y)
    """
    print(f"SPELL CONTROL {cible.id} {x} {y}")
    
# ----------- Constantes et variables

TYPE_MONSTRE = 0
TYPE_MON_HEROS = 1
TYPE_ADV_HEROS = 2


Agent = namedtuple('Agent', [
    'id', 'type', 'x', 'y', 'duree_bouclier', 'sous_controle', 'vie', 'vx', 'vy', 'proche_base', 'menace_pour'
])



# Les coordonnées du coin représentant notre base
ma_base_x, ma_base_y = [int(i) for i in input().split()]
heros_par_joueur = int(input())

# ------------ Boucle du jeu
while True:

    # -------- Récupération des données pour ce tour de jeu

    ma_vie, mon_mana = [int(j) for j in input().split()]
    vie_adv, mana_adv = [int(j) for j in input().split()]
    nombre_agents_visibles = int(input())  # Nombres de heros et monstres visibles

    monstres = []
    mes_heros = []
    adv_heros = []

    for i in range(nombre_agents_visibles):
        _id, _type, x, y, duree_bouclier, sous_controle, vie, vx, vy, proche_base, menace_pour = [int(j) for j in input().split()]
        entity = Agent(
            _id,            # _id: Identifiant unique
            _type,          # _type: 0 = monstre, 1 = mon heros, 2 = heros adverse
            x, y,           # x,y: Position de l'agent
            duree_bouclier, # duree_bouclier: Inutile pour la première ligue. Nombre de tours avant que le bouclier disparaisse
            sous_controle,  # sous_controle: Inutile pour la première ligue. Vaut 1 quand cet agent est sous controle d'un sort
            vie,            # vie: Vie restante de l'agent
            vx, vy,         # vx,vy: Coordonnées du vecteur vitesse de l'agent
            proche_base,    # proche_base: 0 = Le monstre n'a pas de cible, 1 = Le monstre cible une base
            menace_pour     # menace_pour : Etant donné la trajectoire du monstre, le monstre est une menace pour 1 = votre base, 2 = la base adverse, 0 = personne
        )
        
        if _type == TYPE_MONSTRE:
            monstres.append(entity)
        elif _type == TYPE_MON_HEROS:
            mes_heros.append(entity)
        elif _type == TYPE_ADV_HEROS:
            adv_heros.append(entity)


    # ------------------------------------------
    # ------------- Logique du jeu -------------
    # ------------------------------------------

    for numero_heros in range(heros_par_joueur):

        cible = None
        if monstres:
            cible = monstres[0]
        
        
        if cible:
            aller_vers_cible(cible)
        else:
            attendre()
            
  

            
