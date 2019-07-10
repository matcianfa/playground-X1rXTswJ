from pendu import * # On  importe les fonctions créées
import random # Pour choisir aléatoirement
from ma_bao import * # Simplement pour les fonctions fail() et success() qui modifie la couleur de la barre à le fin

# --------------------- Constantes
#On charge le dictionnaire ne contenant que les mots entre 7 et 10 lettres
with open("TP/dictionnaire7-10.txt",mode="r", encoding = "ISO-8859-1") as dic:
    dico=[mot.rstrip('\n') for mot in dic]
    
nb_erreurs_max=7 # Maximum d'erreur possible avant d'etre pendu
mot_choisi= random.choice(dico) # On choisit un mot au hasard dans notre dictionnaire
mot_partiel="_"*len(mot_choisi) # On crée notre mot caché en remplaçant toutes les lettres par des _

#--------------------- Les graphiques (3D bien sûr)
graphiques=["  --------------\n    |        \n    |        \n    |       \n    |       \n    |      \n    |        \n    |        \n    |       \n   /|\     \n  / | \ \n /  |  \ \n~~~~~~~~~~~~~~~~~~~~~\n","  --------------\n    |        |\n    |        |\n    |       \n    |       \n    |      \n    |        \n    |        \n    |       \n   /|\     \n  / | \ \n /  |  \ \n~~~~~~~~~~~~~~~~~~~~~\n","  --------------\n    |        |\n    |        |\n    |       / \ \n    |       \_/\n    |      \n    |        \n    |        \n    |       \n   /|\     \n  / | \ \n /  |  \ \n~~~~~~~~~~~~~~~~~~~~~\n","  --------------\n    |        |\n    |        |\n    |       / \ \n    |       \_/\n    |        |\n    |        |\n    |        |\n    |       \n   /|\    \n  / | \ \n /  |  \ \n~~~~~~~~~~~~~~~~~~~~~\n","  --------------\n    |        |\n    |        |\n    |       / \ \n    |       \_/\n    |      __|\n    |        |\n    |        |\n    |       \n   /|\     \n  / | \ \n /  |  \ \n~~~~~~~~~~~~~~~~~~~~~\n","  ------\--------\n    |        |\n    |        |\n    |       / \ \n    |       \_/\n    |      __|__\n    |        |\n    |        |\n    |       \n   /|\     \n  / | \ \n /  |  \ \n~~~~~~~~~~~~~~~~~~~~~\n","  --------------\n    |        |\n    |        |\n    |       / \ \n    |       \_/\n    |      __|__\n    |        |\n    |        |\n    |       / \n   /|\     /   \n  / | \ \n /  |  \ \n~~~~~~~~~~~~~~~~~~~~~\n","  --------------\n    |        |\n    |        |\n    |       / \ \n    |       \o/\n    |      __|__\n    |        |\n    |        |\n    |       / \ \n   /|\     /   \ \n  / | \ \n /  |  \ \n~~~~~~~~~~~~~~~~~~~~~\n"]



if __name__ == "__main__": 
    nb_erreurs = 0 # Pour compter le nombre d'erreur
    print(graphiques[nb_erreurs])
    while "_" in mot_partiel and nb_erreurs < nb_erreurs_max :
        print("\nMot à trouver :",espacer(mot_partiel))
        lettre=input("Donner une lettre : ").upper()

        # Si la lettre a déjà été trouvée, on retente
        if lettre in mot_partiel :
            print("Lettre déjà utilisée")

        # Si la lettre est dans le mot
        elif lettre in mot_choisi:
            mot_partiel=ajouter_lettre(lettre,mot_partiel,mot_choisi)
            print(lettre,"est bien dans le mot")

        # Si on s'est trompé
        else :
            nb_erreurs+=1
            print(lettre,"n'est pas dans le mot")
            print("Vous avez faire {} erreurs sur {}".format(nb_erreurs,nb_erreurs_max))
        print(graphiques[nb_erreurs])

    if "_" in mot_partiel :
        print("Perdu!")
        print("Le mot était ", mot_choisi)
        print("TECHIO> success false") # Fonction interne à ce site : pour afficher la barre en rouge
    else :
        print("Bravo !")
        print("TECHIO> success true") # Fonction interne à ce site : pour afficher la barre en vert
