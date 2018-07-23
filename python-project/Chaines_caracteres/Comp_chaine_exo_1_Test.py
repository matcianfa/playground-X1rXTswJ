#Ne pas oublier de changer le module à importer
module="Chaines_caracteres/Comp_chaine_exo_1"

import sys
import io
from ma_bao import *

sauvegarde_stdout=sys.stdout
sys.stdout=io.StringIO()
import Comp_chaine_exo_1
count1 = sys.stdout.getvalue()[:-1].split("\n")
sys.stdout=sauvegarde_stdout


solution=[ord(car) for car in Comp_chaine_exo_1.texte]

#message d'aide si besoin
help=""

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
      for i in range(max(len(count1),len(solution))):
        assert str(count1[i]) == str(solution[i]), "Le résultat obtenu est {} au lieu de {}".format(str(count1[i]),str(solution[i]))
        send_msg("Tests validés","Le résultat obtenu est bien {}".format(str(count1[i])))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
    except IndexError as e:
      fail()
      send_msg("Aide", "Attention : range(100) donne les entiers de 0 à 99 !")
      


if __name__ == "__main__": test()
