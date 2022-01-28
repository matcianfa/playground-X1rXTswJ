# ------------- Les imports
import sys


# ------------- Les fonctions auxiliaires
def log(*x):
    """
    Permet d'afficher des données utiles comme un message d'erreur (et donc qui ne sera pas considéré comme une réponse)
    Ex : log(a,b,c) affichera les valeurs de a, b et c
    """
    print(*x, file=sys.stderr)


# ------------- Les constantes variables

# --- Cases particulières
CORBEILLE_MYRTILLES = "B"
CORBEILLE_GLACE = "I"
FENETRE = "W"
TABLE_VIDE = "#"
LAVE_VAISSELLE = "D"
SOL = "."
CORBEILLE_FRAISES = "S"
PLANCHE_A_DECOUPER = "C"
FOUR = "O"
CORBEILLE_PATE="H"

# --- Objets
VIDE = "NONE"
ASSIETTE = "DISH"
GLACE = "ICE_CREAM"
MYRTILLES = "BLUEBERRIES"
FRAISES = "STRAWBERRIES"
FRAISES_DECOUPEES = "CHOPPED_STRAWBERRIES"
PATE = "DOUGH"
CROISSANT = "CROISSANT"
PATE_COUPEE = "CHOPPED_DOUGH"
TARTE_CRUE = "RAW_TART"
TARTE = "TART"

# --- Autre
NB_CASES = 7*11

# --- Variables pour les cases
# On numerote les cases de 0 à 76 pour les identifier.
# Remarque : Pour les coordonnées, (0,0) est la case en haut à gauche, (1,0) est celle sur sa droite alors que (0,1) est celle en dessous.

cases_x = []
cases_y = []
cases_nom = []
cases_objet = []

# --- Variables pour les joueurs

joueur_x = 0
joueur_y = 0
joueur_objet = VIDE

partenaire_x = 0
partenaire_y = 0
partenaire_objet = VIDE

# --- Variables pour le jeu

commandes = []
recompenses = []


# ------------- Fonctions pour le jeu


def donner_case_par_nom(nom):
    """
    Renvoie le numero de la case du jeu qui correspond au nom
    """
    for i in range(NB_CASES):
        if cases_nom[i] == nom:
            return i

def donner_case_par_objet(objet):
    """
    Renvoie le numero de la case du jeu qui contient l'objet
    """
    for i in range(NB_CASES):
        if cases_objet[i] == objet:
            return i


def donner_case_par_coord(x, y):
    """
    Renvoie le numero de la case de coordonnées (x,y)
    """
    for i in range(NB_CASES):
        if cases_x[i] == x and cases_y[i] == y:
            return i


def utiliser(case):
    print("USE", cases_x[case], cases_y[case])


def aller(case):
    print("MOVE", cases_x[case], cases_y[case])


def attendre():
    print("WAIT")



# ------------- Le jeu

# ------ Récupération des données d'entrée communes pour toute la partie
# --- Les données correspondant aux clients
nb_clients = int(input())
for i in range(nb_clients):
    # commande_client: Le plat commandé par le client
    # recompense_client: Le nombre de points que rapportera la commande
    commande_client, recompense_client = input().split()
    recompense_client = int(recompense_client)

# --- Entrées pour la cuisine 
for y in range(7):
    ligne_cuisine = input()
    for x, nom in enumerate(ligne_cuisine):
        cases_x.append(x)
        cases_y.append(y)
        cases_nom.append(nom)
        cases_objet.append(VIDE)

# ------ Boucle du jeu
while True:
    # --- Réinitialisation
    commandes = []
    recompenses = []
    cases_objet = [VIDE]*NB_CASES

    tours_restants = int(input())

    # --- Mise à jour des données du joueur
    joueur_x, joueur_y, joueur_objet = input().split()
    joueur_x = int(joueur_x)
    joueur_y = int(joueur_y)

    # --- Mise à jour des données du partenaire
    partenaire_x, partenaire_y, partenaire_objet = input().split()
    partenaire_x = int(partenaire_x)
    partenaire_y = int(partenaire_y)

    # --- Mise à jour des données des tables
    nb_tables_avec_objets = int(input())  # Le nombre de tables contenant un objet
    for i in range(nb_tables_avec_objets):
        table_x, table_y, objet = input().split()
        table_x = int(table_x)
        table_y = int(table_y)
        case = donner_case_par_coord(table_x, table_y)
        cases_objet[case] = objet

    # --- Contenu du four ( Utile à partir de la ligue Bois 1)
    contenu_four, minuteur_four = input().split()
    minuteur_four = int(minuteur_four)

    # --- Les commandes des clients en attente
    nb_clients = int(input())  # Le nombre de clients qui attendent leur commande
    for i in range(nb_clients):
        commande_client, recompense_client = input().split()
        recompense_client = int(recompense_client)
        commandes.append(commande_client)
        recompenses.append(recompense_client)


    # --- Logique du jeu : C'est ici qu'il faut compléter le code pour gérer le cuisinier
    # Exemple : pour récupérer l'assiette et la glace :
    if ASSIETTE not in joueur_objet:
        utiliser(donner_case_par_nom(LAVE_VAISSELLE))
    elif GLACE not in joueur_objet:
        utiliser(donner_case_par_nom(CORBEILLE_GLACE))
    else:
        attendre()
