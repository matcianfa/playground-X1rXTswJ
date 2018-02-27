#Ne pas oublier de changer le module à importer
from Champernowne import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
(1,0.1),\
(2,0.12),\
(7,0.1234567),\
(10,"0.12345678910"),\
(100,0.123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100"),\
(0,0)\
]


#message d'aide si besoin
help="Attention si n est nul, le nombre de Champernowne vaut 0 aussi"



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
        count1 = sys.stdout.getvalue()
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp), "En testant la valeur {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant la valeur {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
