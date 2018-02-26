#Ne pas oublier de changer le module à importer
from Conversion_Celsius_Fahrenheit import mon_programme 
import sys
import io


#liste des couples input/output
input_output=[\
((0,0),32.0),\
((100,0),212.0),\
((0,1),-17.778),\
((100,1),37.778),\
((37,0),98.6),\
((-273.15,0),-459.67)\
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
        assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","La température {}°"+"C"*(inp[1]==0)+"F"*(inp[1]==1)+" correspond bien à {}°"+"C"*(inp[1]==1)+"F"*(inp[1]==0).format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__":
test()
