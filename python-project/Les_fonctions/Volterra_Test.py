#Ne pas oublier de changer le module à importer
from Volterra import u,v
import sys
import io


#liste des couples input/output
input_output=[\
(1,204.0,57.49999999999999),\
(3,211.249851246,76.82409376999999),\
(10,217.9385763255597,227.066780089635),\
(15,184.29606095667762,472.6175497356709)\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,rep_u,rep_v in input_output:
        assert u(inp) == rep_u and v(inp)==rep_v, "En testant pour n={} le résultat obtenu pour u(n) est {} au lieu de {} et pour v(n) est {} au lieu de {}".format(str(inp),str(u(n)),str(rep_u),str(v(n)),str(rep_v))
        send_msg("Tests validés","En testant pour n={} le résultat obtenu pour u(n) est bien {} et pour v(n) est bien {}".format(str(inp),str(rep_u),str(rep_v)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
