#Ne pas oublier de changer le module à importer
from fonction_binom import binom as f
import sys
import io


#liste des couples input/output
input_output=[\
((4,2),6),\
((10,0),1),\
((3,3),1),\
((8,4),70),\
((2,4),0)\
]



#message d'aide si besoin
help="N'oublie pas d'utiliser return pour afficher le resultat. Utilisez int() pour transformer les flottants en entiers."



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for x,reponse in input_output:
        assert f(*x) == reponse, "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(x),str(f(*x)),str(reponse))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(x),str(f(*x))))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
