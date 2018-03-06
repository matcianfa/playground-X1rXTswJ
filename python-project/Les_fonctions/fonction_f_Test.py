#Ne pas oublier de changer le module à importer
from fonction_f import f
import sys
import io


#liste des couples input/output
input_output=[-1.,0.,0.5,1.,2.,1/3]

#la fonction attendue:
def reponse(x):
  return 3*x**2-2*x-1

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
