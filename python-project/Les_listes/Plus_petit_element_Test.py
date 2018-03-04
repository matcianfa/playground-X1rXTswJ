#Ne pas oublier de changer le module à importer
from Plus_petit_element import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
([4,2,7,5],[1]),\
([4,2,7,5,2,7,10,2,6,2],[1,4,7,9]),\
([5,4,3,2,1,2,3,4,5,4,3,2,1],[4,12]),\
([1000000000],[0]),\
([1,1,1,1,1,1,1,1],[0,1,2,3,4,5,6,7])\
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
