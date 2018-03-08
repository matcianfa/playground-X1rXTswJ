#Ne pas oublier de changer le module à importer
from Algo_Kaprekar import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
(326,[495]),\
(1234,[6174]),\
(123456,[851742, 750843, 840852, 860832, 862632, 642654, 420876]),\
(326262351,[863098632, 965296431, 873197622, 865395432, 753098643, 954197541, 883098612, 976494321, 874197522, 865296432, 763197633, 844296552, 762098733, 964395531]),\
(123456789,[864197532]),\
(2222,[0]),\
(34,[9, 81, 63, 27, 45])\
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
        assert str(sorted(eval(count1))) == str(sorted(outp)), "En testant la valeur {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant la valeur {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
