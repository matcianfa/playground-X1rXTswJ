#Ne pas oublier de changer le module à importer
module="Les_boucles/for_exo_2"

import sys
import io
from ma_bao import *
import for_exo_2

solution=sum([i*i for i in range(5,124)])

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
      if str(count1) == str(sum([i*i for i in range(5,123)])):
        send_msg("Aide 💡", "Attention, quand on écrit range(5,123), on calcule la somme de 5 à 122 !")


if __name__ == "__main__": test()
