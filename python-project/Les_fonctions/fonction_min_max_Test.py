#Ne pas oublier de changer le module à importer
from fonction_min_max import min_max as f
import sys
import io


#liste des couples input/output
input_output=[(1,3),(3,1),(1,1),(4,-4)]


#la fonction attendue:
def reponse(a,b):
  return (min(a,b),max(a,b))

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
        assert f(*x) == reponse(*x), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(x),str(f(*x)),str(reponse(*x)))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(x),str(f(*x))))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
