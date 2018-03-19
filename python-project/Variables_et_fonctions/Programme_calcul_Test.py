#Ne pas oublier de changer le module à importer
module="Variables_et_fonctions/Programme_calcul"
from Programme_calcul import mon_programme
import sys
import io


#liste des couples input/output
input_output=[0,1,5,18,-3]

def verif(n):
  reponses=[]
  x=n-3
  reponses.append(x)
  y=x*2
  reponses.append(y)
  z=y**2
  reponses.append(z)
  a = z/10
  reponses.append(a)
  reponse=n+x+y+z+a
  reponses.append(reponse)
  return reponses
  
consignes=[\
"Soustraire 3 à n et sauvegarder le résultat dans x. Ensuite, afficher x",\
"Multiplier x par 2 et sauvegarder le résultat dans y. Ensuite, afficher y",\
"Mettre y au carré et sauvegarder le résultat dans z. Ensuite, afficher z",\
"Diviser z par 10 et sauvegarder le résultat dans a. Ensuite, afficher a",\
"Ajouter n, x, y, z et a et sauvegarder le résultat dans reponse. Ensuite, afficher reponse"\
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
        rep = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        for i in range(5):
          assert str(rep[i]) == str(corr[i]), consignes[i]
      success()
    except AssertionError as e:
      fail()
      send_msg("Instructions", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
