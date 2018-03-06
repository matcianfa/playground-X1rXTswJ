#Ne pas oublier de changer le module à importer
from fonction_approx_e import approx_e as f
import sys
import io


#liste des couples input/output
input_output=[\
(2,2.5),\
(5,2.7166666666666663),\
(7,2.7182539682539684),\
(20,2.7182818284590455),\
(200,2.7182818284590455),\
(0,1),\
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
