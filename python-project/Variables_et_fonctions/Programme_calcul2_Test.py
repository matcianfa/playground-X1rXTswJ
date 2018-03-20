#Ne pas oublier de changer le module à importer
module="Variables_et_fonctions/Programme_calcul2"
from math import *
import sys
import io
from ma_bao import *
tester("from Programme_calcul2 import mon_programme",globals())

#liste des couples input/output
input_output=[0,1,5,18,-3]

def verif(n):
  reponses=[]
  a=n+pi
  reponses.append(a)
  b=sqrt(a)
  reponses.append(b)
  c=round(b,5)
  reponses.append(c)
  d= cos(a/2)
  reponses.append(d)
  e=round(d,5)
  reponses.append(e)
  f=a+c+e
  reponses.append(f)
  reponses.append('')
  return reponses
  
consignes=[\
"Ajouter pi à n et sauvegarder le résultat dans a. Ensuite, afficher a",\
"Calculer la racine carrée de a et sauvegarder le résultat dans b. Ensuite, afficher b",\
"Calculer l'arrondi de b à 5 chiffres après la virgule et sauvegarder le résultat dans c. Ensuite, afficher c",\
"Calculer le cosinus de a/2 et sauvegarder le résultat dans d. Ensuite, afficher d",\
"Calculer l'arrondi de d à 5 chiffres après la virgule et sauvegarder le résultat dans e. Ensuite, afficher e",\
"Calculer la somme de a, c et e et sauvegarder le résultat dans f. Ensuite, afficher f",\
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
