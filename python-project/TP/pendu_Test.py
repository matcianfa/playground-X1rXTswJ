from pendu import * # On  importe les fonctions créées
import random # Pour choisir aléatoirement

# --------------------- Constantes
#On charge le dictionnaire ne contenant que les mots entre 7 et 10 lettres
with open("TP/dictionnaire7-10.txt",mode="r") as dic:
    dico=[mot.rstrip('\n') for mot in dic]
    
nb_erreurs_max=7 # Maximum d'erreur possible avant d'etre pendu
mot_choisi= random.choice(dico) # On choisit un mot au hasard dans notre dictionnaire
mot_partiel="_"*len(mot_complet) # On crée notre mot caché en remplaçant toutes les lettres par des _


if __name__ == "__main__": 
    nb_erreurs = 0 # Pour compter le nombre d'erreur
    while "_" in mot_partiel and nb_erreurs < nb_erreurs_max :
        print("\nMot à trouver :",espacer(mot_partiel))
        lettre=input("Donner une lettre").upper()

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

    if "_" in mot_partiel :
        print("Perdu!")
        print("Le mot était ", mot_choisi)
    else :
        print("Bravo !")
