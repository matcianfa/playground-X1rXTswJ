from Passage_polaires_cartesiennes import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
((1,90),"0.0 1.0"),\
((2,45),"1.414 1.414"),\
((3,-30),"2.598 -1.5"),\
((1,0),"1.0 0.0")\
((4,135),"-2.828 2.828")\
((1,3.14159),"0.998 0.055")\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print(x,y) pour afficher le resultat. Attention à bien changer les angles en radians aussi."



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


if __name__ == "__main__":
   test()
