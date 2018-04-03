#Ne pas oublier de changer le module à importer
module="Optimisation/tri_fib"

import sys
import io
from ma_bao import *
tester("from tri_fib import *",globals())

#liste des couples input/output
input_output=[\
(1,1),\
(2,1),\
(3,3),\
(5,9),\
(10,193),\
(100,127071617887002752149434981),\
(500,920080768385554537118362247382795511748094060211249395714846663504876568933187764773247307152478284645110957568578400676655207195125)\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"



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
      for inp,outp in input_output:
        count1 = tri_fib(inp)
        assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
