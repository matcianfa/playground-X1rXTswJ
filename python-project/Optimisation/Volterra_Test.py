#Ne pas oublier de changer le module à importer
module="Optimisation/Volterra"

import sys
import io
from ma_bao import *
tester("from Volterra import u,v",globals())


#liste des couples input/output
input_output=[\
(1,53000.0,9135.000000000002),\
(3,52784.4713838875,9407.788308056253),\
(10,50106.76034377454,10027.348268924994),\
(15,47682.76719143467,9802.229920404247),\
(50,51931.6642577963,10510.241252724509),\
(250,49366.47252096073,1235.4228635547697),\
(350,1148.9214047535777,185.0045533350926)\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser return pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")    
     afficher_correction(module)
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,rep_u,rep_v in input_output:
        assert u(inp) == rep_u and v(inp)==rep_v, "En testant pour n={} le résultat obtenu pour u(n) est {} au lieu de {} et pour v(n) est {} au lieu de {}".format(str(inp),str(u(inp)),str(rep_u),str(v(inp)),str(rep_v))
        send_msg("Tests validés","En testant pour n={} le résultat obtenu pour u(n) est bien {} et pour v(n) est bien {}".format(str(inp),str(rep_u),str(rep_v)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
