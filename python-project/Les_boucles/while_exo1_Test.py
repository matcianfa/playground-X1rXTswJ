#Ne pas oublier de changer le module à importer
module="Les_boucles/while_exo1"

import sys
import io
from ma_bao import *

sauvegarde_stdout=sys.stdout
sys.stdout=io.StringIO()
import while_exo1
count1 = sys.stdout.getvalue()[:-1]
sys.stdout=sauvegarde_stdout

solution=0
while (solution+1)*(solution+3)<12345 :
    solution+=1

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
      assert str(count1) == str(solution), "Le résultat obtenu est {} mais ce n'est pas le bon".format(str(count1))
      send_msg("Tests validés","Le résultat obtenu est bien {}".format(str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if str(count1) == str(sum([i for i in range(3,172)])):
        send_msg("Aide 💡", "Attention, quand on écrit range(3,172), on calcule la somme de 3 à 171 !")


if __name__ == "__main__": test()
