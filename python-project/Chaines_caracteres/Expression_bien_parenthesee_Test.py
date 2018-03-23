#Ne pas oublier de changer le module à importer
module="Les_boucles/Expression_bien_parenthesee"

import sys
import io
from ma_bao import *
tester("from Expression_bien_parenthesee import mon_programme",globals())




#liste des couples input/output
input_output=[\
("(1+x)","BIEN PARENTHESEE"),\
("(x+1)*(2-x)","BIEN PARENTHESEE"),\
("(1+x)/4)*(2+(x+1)","MAL PARENTHESEE"),\
("(()()(","MAL PARENTHESEE"),\
("cos((1+x)/2)*(2+x)","BIEN PARENTHESEE"),\
("(((()()())((())())())(()()))","BIEN PARENTHESEE"),\
("x+1*x/5*cos x","BIEN PARENTHESEE")\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    afficher_correction()
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
