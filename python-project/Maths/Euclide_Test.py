#Ne pas oublier de changer le module à importer
from Euclide import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
((12,6),6),\
((24,10),2),\
((21,13),1),\
((21,0),21),\
((0,13),13),\
((36,60),12)\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser return pour afficher le resultat. Attention à l'ordre de a et b"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp in input_output:
        count1 =mon_programme(*inp)
        assert count1 == outp, "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
