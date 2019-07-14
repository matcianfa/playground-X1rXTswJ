from pendu import * # On  importe les fonctions créées
import random # Pour choisir aléatoirement


# --------------------- Constantes
#On charge le dictionnaire ne contenant que les mots entre 7 et 10 lettres
with open("TP/dictionnaire7-10.txt",mode="r") as dic:
    dico=[mot.rstrip('\n') for mot in dic]
    
nb_erreurs_max=7 # Maximum d'erreur possible avant d'etre pendu
longueur=random.randint(7,10) # longueur du mot
mot_partiel="_"*longueur # On crée notre mot caché en remplaçant toutes les lettres par des _
lettres_proposees=[]

#--------------------- Les graphiques (3D bien sûr)
graphiques=["  --------------\n    |        \n    |        \n    |       \n    |       \n    |      \n    |        \n    |        \n    |       \n   /|\     \n  / | \ \n /  |  \ ","  --------------\n    |        |\n    |        |\n    |       \n    |       \n    |      \n    |        \n    |        \n    |       \n   /|\     \n  / | \ \n /  |  \ ","  --------------\n    |        |\n    |        |\n    |       / \ \n    |       \_/\n    |      \n    |        \n    |        \n    |       \n   /|\     \n  / | \ \n /  |  \ ","  --------------\n    |        |\n    |        |\n    |       / \ \n    |       \_/\n    |        |\n    |        |\n    |        |\n    |       \n   /|\    \n  / | \ \n /  |  \ ","  --------------\n    |        |\n    |        |\n    |       / \ \n    |       \_/\n    |      __|\n    |        |\n    |        |\n    |       \n   /|\     \n  / | \ \n /  |  \ ","  ---------------\n    |        |\n    |        |\n    |       / \ \n    |       \_/\n    |      __|__\n    |        |\n    |        |\n    |       \n   /|\     \n  / | \ \n /  |  \ ","  --------------\n    |        |\n    |        |\n    |       / \ \n    |       \_/\n    |      __|__\n    |        |\n    |        |\n    |       / \n   /|\     /   \n  / | \ \n /  |  \ ","  --------------\n    |        |\n    |        |\n    |       / \ \n    |       \o/\n    |      __|__\n    |        |\n    |        |\n    |       / \ \n   /|\     /   \ \n  / | \ \n /  |  \ "]



if __name__ == "__main__": 
    nb_erreurs = 0 # Pour compter le nombre d'erreur
    print(graphiques[nb_erreurs])
    while "_" in mot_partiel and nb_erreurs < nb_erreurs_max :
        print("\nMot à trouver :",espacer(mot_partiel))
        lettre=input("Donner une lettre : ").upper()

        # Si la lettre a déjà été proposée, on retente
        if lettre in lettres_proposees :
            print("Lettre déjà proposée, rejouez !")
            continue
        
        # On propose le nouveau mot_partiel
        mot_partiel_2= ajouter_lettre(lettre,lettres_proposees,mot_partiel,dico)
        
        # Si ce n'est pas le même :
        if mot_partiel!=mot_partiel2:
            mot_partiel=mot_partiel2
            print(lettre,"est bien dans le mot")

        # Si c'est le même, on s'est trompé
        else :
            nb_erreurs+=1
            print(lettre,"n'est pas dans le mot")
            print("Vous avez fait {} erreurs sur {}".format(nb_erreurs,nb_erreurs_max))
        lettres_proposees.append(lettre)
        print(graphiques[nb_erreurs])

    if "_" in mot_partiel :
        print("Perdu!")
        print("Le mot était ", donner_mot(lettres_proposees,mot_partiel,dico))
    else :
        print("Bravo ! C'était bien ", mot_partiel)
