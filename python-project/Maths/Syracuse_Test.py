#Ne pas oublier de changer le module à importer
from Syracuse import syracuse as f
import sys
import io


#liste des couples input/output
input_output=[\
(5,[5, 16, 8, 4, 2, 1]),\
(21,[21, 64, 32, 16, 8, 4, 2, 1]),\
(17,[17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]),\
(15,[15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]),\
(127,[127, 382, 191, 574, 287, 862, 431, 1294, 647, 1942, 971, 2914, 1457, 4372, 2186, 1093, 3280, 1640, 820, 410, 205, 616, 308, 154, 77, 232, 116, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])\
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
        send_msg("Tests validés","La suite de Syracuse qui commence avec {} est bien {}".format(str(x),str(f(x))))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
