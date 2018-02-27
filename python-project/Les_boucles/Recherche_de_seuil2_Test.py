#Ne pas oublier de changer le module à importer
from Recherche_de_seuil2 import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
((1,2),1),\
((2,16),3),\
((0,-1),0),\
((-1,-4),0),\
((3,123456789),26),\
((1,18446744073709551616),64),\
((-1,3),"IMPOSSIBLE"),\
((0,1),"IMPOSSIBLE")\
]


#message d'aide si besoin
help="Bien considérer tous les cas, même pour u_0 et e négatifs"



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
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(*inp)
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
