#Ne pas oublier de changer le module à importer
module="Variables_et_fonctions/Programme_calcul3"
from math import *
import sys
import io
from ma_bao import *
tester("from Programme_calcul3 import mon_programme",globals())

#liste des couples input/output
input_output=[0,1,5,18,-3]

def verif(n):
  reponses=[]
  a=2*n
  reponses.append(a)
  a+=5
  reponses.append(a)
  b = n**2
  reponses.append(b)
  a,b=b,a
  reponses.append(a,b)
  a,b=3*a+1,2*a-b
  reponses.append(a,b)
  reponses.append('')
  return reponses
  
consignes=[\
"Calculer le double de n et sauvegarder le résultat dans a. Ensuite, afficher a",\
"Augmenter a de 5 et afficher a",\
"Calculer le carré de n et sauvegarder le résultat dans b. Ensuite, afficher b",\
"Inverser les valeurs de a et b. Ensuite, afficher a et b sur une seule ligne, séparés d'un espace",\
"Calculer 3a+1 et 2a-b et sauvegarder le résultat dans a et b respectivement. Ensuite, afficher a et b sur une seule ligne, séparés d'un espace",\
"C'est terminé !"\
]

#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"

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
      for n in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(n)
        corr=verif(n)
        rep = sys.stdout.getvalue().split("\n")
        sys.stdout=sauvegarde_stdout
        for i,reponse in enumerate(rep):
          assert str(reponse) == str(corr[i]), consignes[i]
      success()
    except AssertionError as e:
      fail()
      send_msg("Instructions", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
