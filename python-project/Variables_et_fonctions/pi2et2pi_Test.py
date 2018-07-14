#Ne pas oublier de changer le module à importer
module="Variables_et_fonctions/pi2et2pi"
import sys
import io
#On récupère les données de l'utilisateur
sauvegarde_stdout=sys.stdout
sys.stdout=io.StringIO()
from pi2et2pi import *
count1 = sys.stdout.getvalue()[:-1]
sys.stdout=sauvegarde_stdout
from ma_bao import *

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
reponse=max(2**pi,pi**2)


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
      assert str(count1) == str(reponse), "Le résultat obtenu est {} mais ce n'est pas le bon.".format(str(count1))
      send_msg("Tests validés","Le résultat cherché est bien {}".format(str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
