#Ne pas oublier de changer le module à importer
from Suite_recurrente_simple import u as f
import sys
import io


#liste des couples input/output
input_output=[\
(0,2),\
(1,7),\
(2,17),\
(3,37),\
(4,77)\
]



#message d'aide si besoin
help="N'oublie pas d'utiliser return pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo ! Les premières décimales de e sont 2, 71828182845904523536 ...")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for x,reponse in input_output:
        assert f(x) == reponse, "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(x),str(f(x)),str(reponse))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(x),str(f(x))))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
