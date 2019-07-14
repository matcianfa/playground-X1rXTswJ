# A modifier si besoin
nom_fonction="ajouter_lettre"

# Test un peu particulier : On vérifie juste que la fonction proposée donne un mot_partiel satisfaisant les conditions.

#On charge le dictionnaire ne contenant que les mots entre 7 et 10 lettres
with open("TP/dictionnaire7-10.txt",mode="r") as dic:
    dico=[mot.rstrip('\n') for mot in dic]

#liste des valeurs à tester
# Attention de bien mettre dans un tuplet ou une liste les valeurs à tester même si la fonction n'a qu'un argument.
valeurs_a_tester=["[E","A Z R T Y U P Q S D".split(),"_______",dico],["M",["U","A","I","X","Z","C","Y","V","K"],"_AI____",dico],["M","L A Z E R T Y U I O P Q S".split(),"_AISONS",dico]]

def verif(mot2,lettre,lettres,mot_partiel,dictionnaire):
    """
    Vérifie si le mot proposé vérifie les critères
    """
    reponses=[]
    lettre_proposees=lettres+[lettre]
    # On vérifie qu'on a bien rajouté la bonne lettre
    longueur = len(mot_partiel)
    if len(mot2)!=longueur : return False
    for i in range(longueur):
        if (mot_partiel[i]=="_" and mot2[i] not in "_"+lettre ) or (mot_partiel!="_" and mot_partiel!=mot2[i]):
            return False
    # On vérifie qu'il existe bien des mots dans le dictionnaire qu'on puisse ecrire
    for mot in dictionnaire :
        if len(mot)!= longueur : continue
        for i in range(longueur):
            if (mot2[i]=="_" and (mot[i] in lettres_proposees or mot[i] in mot2)) or ( mot2[i]!="_" and mot2[i]!=mot[i] ):
                break
        else :
            reponses.append(mot)
    if reponses:
        return True
    else : return False


#message d'aide si besoin
help="N'oublie pas d'utiliser return pour renvoyer le resultat."

#------------------------------------
# Les imports
import sys
# Ma boite à outils
from ma_bao import * 
# Donne les noms du dossier et du module (automatiquement avec __file__
chemin,module=donner_chemin_nom(__file__)
# On teste s'il n'y a pas d'erreurs de synthaxe etc. et on les montre si besoin
tester("from {} import *".format(module),globals()) 
from donner_solution import donner_solution as f

#--------------------------------------
def test():
    try:
        for valeur in valeurs_a_tester:
            rep=f(*valeur)
            assert verif(rep,*valeur), "En testant les valeurs {} le mot proposé est {} mais ce n'est pas bon".format(",".join([str(val) for val in valeur[:2]]),str(rep))
            send_msg("Tests validés","En testant les valeurs {} le mot proposé est {}".format(",".join([str(val) for val in valeur[:2]]),str(rep)))
        success(chemin+module)
    except AssertionError as e:
        fail()
        send_msg("Oops! ", e)
        if help:
            send_msg("Aide 💡", help)

#--------------------------------------
if __name__ == "__main__": test()
