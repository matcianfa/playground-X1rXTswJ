#Ne pas oublier de changer le module à importer
from Triangles_constructibles import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
((3,4,5),"CONSTRUCTIBLE"),\
((3,5,4),"CONSTRUCTIBLE"),\
((5,3,4),"CONSTRUCTIBLE"),\
((1,1,5),"PAS CONSTRUCTIBLE"),\
((5,1,1),"PAS CONSTRUCTIBLE"),\
((5.5,4.5,3.5),"CONSTRUCTIBLE"),\
((2,1,1),"PLAT"),\
((2,1,3),"PLAT"),\
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
        mon_programme(*inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp) or (outp=="PLAT" and str(count1)=="CONSTRUCTIBLE"), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        if str(count1)=="PLAT":
          send_msg("Tests validés", "Très bien, le triangle {} est bien plat !".format(str(inp)))
        else:
          send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
