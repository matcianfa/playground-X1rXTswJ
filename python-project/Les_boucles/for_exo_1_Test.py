#Ne pas oublier de changer le module à importer
module="Les_boucles/for_exo_1"

import sys
import io
from ma_bao import *

sauvegarde_stdout=sys.stdout
sys.stdout=io.StringIO()
tester("from for_exo_1 import mon_programme",globals())
count1 = sys.stdout.getvalue()[:-1]
sys.stdout=sauvegarde_stdout

solution=sum([i for i in range(3,173)])

#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"

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
      assert str(count1) == str(solution), "En testant les valeurs {} le résultat obtenu est {} mais ce n'est pas le bon".format(str(inp),str(count1))
      send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
