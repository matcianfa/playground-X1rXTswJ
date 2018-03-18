#Ne pas oublier de changer le module à importer
module="Defis/Euler_1"
import sys
import io
sauvegarde_stdout=sys.stdout
sys.stdout=io.StringIO()
#mon_programme(*inp)
from Euler_1 import *
count1 = sys.stdout.getvalue()[:-1]
sys.stdout=sauvegarde_stdout




#La réponse
reponse=233168


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
      '''
      sauvegarde_stdout=sys.stdout
      sys.stdout=io.StringIO()
      #mon_programme(*inp)
      from Euler_1 import *
      count1 = sys.stdout.getvalue()[:-1]
      sys.stdout=sauvegarde_stdout'''
      assert str(count1) == str(reponse), "Le résultat obtenu est {} mais ce n'est pas le bon.".format(str(count1))
      send_msg("Tests validés","Le résultat cherché est bien {}".format(str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
