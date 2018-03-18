#Ne pas oublier de changer le module à importer
module="bac_a_sable"
from bac_a_sable import *
import sys
import io


#liste des couples input/output
input_output=[\
((1,5,6),2),\
((1,1,8),0),\
((1,-2,1),1),\
((0.25,1.25,1.5),2)\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"

#Afficher la correction
def afficher_correction():
    with open(module+"_Correction.txt", "r") as correction :
        ligne="Voici un ou des exemples de corrections possibles"
        send_msg("Exemple(s) de correction", ligne)
        ligne="-------------------------------------------------"
        send_msg("Exemple(s) de correction", ligne)
        while ligne:
            ligne=correction.readline()
            send_msg("Exemple(s) de correction", ligne)

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
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
