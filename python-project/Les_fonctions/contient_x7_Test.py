#Ne pas oublier de changer le module à importer
from fonction_contient_x7 import contient_x7 as f
import sys
import io


#liste des couples input/output
input_output=[\
[7],\
[6],\
[1,7],\
[1,7,14,1],\
[4,21,5,14],\
[1,2,19,231],\
[100,101,99,102]\
]

#la fonction attendue:
def reponse(liste):
  for n in liste:
    if n%7==0:
      return True
  return False

#message d'aide si besoin
help="N'oublie pas d'utiliser return pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for x in input_output:
        assert f(x) == reponse(x), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(x),str(f(x)),str(reponse(x)))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(x),str(f(x))))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
