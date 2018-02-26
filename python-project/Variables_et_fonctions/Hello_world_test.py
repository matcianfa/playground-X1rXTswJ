#Ne pas oublier de changer le module à importer
from Triangles_constructibles import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
((3,4),"Hello World")\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat et de le décaler."



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
        assert str(count1) == str(outp), "Vous avez affiché {} au lieu de {}".format(str(count1),str(outp))
        send_msg("Tests validés","Très bien !")
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
