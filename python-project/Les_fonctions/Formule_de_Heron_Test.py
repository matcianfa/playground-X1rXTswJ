#Ne pas oublier de changer le module à importer
from Formule_de_Heron import racine as f
import sys
import io


#liste des couples input/output
input_output=[\
(1,1.0),\
(2,1.414213562373095),\
(3,1.7320508075688772),\
(5,2.236067977499978),\
(10,3.162277665175675),\
(50,7.072628275743689)\
]



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
      for x,reponse in input_output:
        assert f(x) == reponse, "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(x),str(f(x)),str(reponse))
        send_msg("Tests validés","En testant les valeurs {} l'approximation est {} alors que la vraie valeur est {}".format(str(x),str(f(x)),str(x**0.5)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
