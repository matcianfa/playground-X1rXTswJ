#Ne pas oublier de changer le module à importer
from Tri_a_bulles import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
([1,5,6],[1,5,6]),\
([3,2,5,7,10,1],[1,2,3,5,7,10]),\
([10,9,8,7,6,5,4,3,2,1],[1,2,3,4,5,6,7,8,9,10]),\
([1],[1])\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat. Attention aux pièges : liste vide et avec un seul élément !"



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
