#Ne pas oublier de changer le module à importer
module="Maths/random_exo_3"
import sys
import io
#On récupère les données de l'utilisateur
sauvegarde_stdout=sys.stdout
sys.stdout=io.StringIO()
from random_exo_3 import *
count1 = eval(sys.stdout.getvalue()[:-1])
sys.stdout=sauvegarde_stdout
#from ma_bao import *

#Afficher la correction
def afficher_correction():
    try:
        with open(module+"_Correction.py", "r") as correction :
            ligne="Voici un ou des exemples de corrections possibles"
            send_msg("Exemple(s) de correction", ligne)
            ligne="-------------------------------------------------"
            send_msg("Exemple(s) de correction", ligne)
            lignes=correction.read().split("\n")
            for ligne in lignes:
                send_msg("Exemple(s) de correction", ligne)
    except:
        pass

#La réponse
reponse=""


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    afficher_correction()
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      assert all([n in ["Pierre","Caillou","Ciseaux"] for n in count1]) and len(count1)==100, "Le résultat obtenu est {} mais il n'est pas valide.".format(str(count1))
      send_msg("Tests validés","Le résultat obtenu est valide. Le voici : {}".format(str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
