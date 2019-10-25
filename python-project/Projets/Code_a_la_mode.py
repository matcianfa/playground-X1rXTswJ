# ------------- Les imports
import sys
import math


# ------------- Les fonctions ucases
def log(*x):
    """
    Permet d'afficher des données ucases comme un message d'erreur (et donc qui ne sera pas considéré comme une réponse)
    Ex : log(a,b,c) affichera les valeurs de a, b et c
    """
    print(*x, file=sys.stderr)


# ------------- Les constantes
# Cases particulières
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

# objets
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

# ------------- Les classes
# Remarque : Pour les coordonnées, (0,0) est la case en haut à gauche, (1,0) est celle sur sa droite alors que (0,1) est celle en dessous.

class Joueur:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.objet = VIDE

class Case:
    def __init__(self, x, y, nom):
        self.x = x
        self.y = y
        self.nom = nom
        self.objet = None


    def __repr__(self):
        """
        Permet d'afficher les informations de la case (avec log )
        """
        return "Case: {} ({},{})".format(self.nom,self.x,self.y)



class Jeu:
    """
    Classe regroupant les données du jeu
    """
    def __init__(self):
        self.joueur = Joueur()
        self.partenaire = Joueur()
        self.cases = []
        self.commandes = [] # La liste des 3 commandes en cours

    def reinitialiser(self) :
        """
        Fonction qui remet à zéro ce qui doit l'être en début de chaque boucle de jeu
        """
        self.commandes = []

    def ajouter_case(self, x, y, nom):
        """
        Ajoute les cases qui ne sont pas vides à la liste des cases du jeu
        """
        if nom != '.':
            self.cases.append(Case(x, y, nom))

    def donner_case_par_nom(self, nom):
        """
        Renvoie la case du jeu qui correspond au nom
        """
        for t in self.cases:
            if t.nom == nom:
                return t

    def donner_case_par_objet(self, objet):
        """
        Renvoie une case du jeu qui contient l'objet
        """
        for t in self.cases:
            if t.objet == objet:
                return t


    def donner_case_par_coord(self, x, y):
        """
        Renvoie la case de coordonnées (x,y)
        """
        for t in self.cases:
            if t.x == x and t.y == y:
                return t

    def maj_joueur(self, x, y, objet):
        self.joueur.x = x
        self.joueur.y = y
        self.joueur.objet = objet

    def maj_partenaire(self, x, y, objet):
        self.partenaire.x = x
        self.partenaire.y = y
        self.partenaire.objet = objet

    def utiliser(self, case):
        print("USE", case.x, case.y)

    def aller(self, case):
        print("MOVE", case.x, case.y)


# ------------- Le jeu
jeu = Jeu()

# ------ Récupération des données d'entrée
# Les données correspondant aux clients
nb_clients = int(input())
for i in range(nb_clients):
    # commande_client: the food the customer is waiting for
    # recompense_client: the number of points awarded for delivering the food
    commande_client, recompense_client = input().split()
    recompense_client = int(recompense_client)

# Entrées pour la cuisine (et création des cases pour le jeu)
for y in range(7):
    ligne_cuisine = input()
    for x, nom in enumerate(ligne_cuisine):
        jeu.ajouter_case(x, y, nom)

# boucle du jeu
while True:
    jeu.reinitialiser()

    tours_restants = int(input())

    # Entrée des joueurs
    # Mise à jour des données du joueur
    joueur_x, joueur_y, joueur_objet = input().split()
    joueur_x = int(joueur_x)
    joueur_y = int(joueur_y)
    jeu.maj_joueur(joueur_x, joueur_y, joueur_objet)

    # Mise à jour des données du partenaire
    partenaire_x, partenaire_y, partenaire_objet = input().split()
    partenaire_x = int(partenaire_x)
    partenaire_y = int(partenaire_y)
    jeu.maj_partenaire(partenaire_x, partenaire_y, partenaire_objet)

    # Mise à jour des données des tables
    for t in jeu.cases:
        t.objet = None
    nb_tables_avec_objets = int(input())  # Le nombre de tables contenant un objet
    for i in range(nb_tables_avec_objets):
        table_x, table_y, objet = input().split()
        table_x = int(table_x)
        table_y = int(table_y)
        jeu.donner_case_par_coord(table_x, table_y).objet = objet

    # Contenu du four ( Utile à partir de la ligue 1)
    contenu_four, minuteur_four = input().split()
    minuteur_four = int(minuteur_four)

    # Les commandes des clients en attente
    nb_clients = int(input())  # Le nombre de clients qui attendent leur commande
    for i in range(nb_clients):
        commande_client, recompense_client = input().split()
        recompense_client = int(recompense_client)
        jeu.commandes.append(commande_client)

    # Logique du jeu : C'est ici qu'il faut compléter le code pour gérer le cuisinier
    # Exemple : pour récupérer l'assiette et la glace :
    if ASSIETTE not in jeu.joueur.objet:
        jeu.utiliser(jeu.donner_case_par_nom(LAVE_VAISSELLE))
    elif GLACE not in jeu.joueur.objet:
        jeu.utiliser(jeu.donner_case_par_nom(CORBEILLE_GLACE))
    else:
        jeu.utiliser(jeu.donner_case_par_nom(TABLE_VIDE))
