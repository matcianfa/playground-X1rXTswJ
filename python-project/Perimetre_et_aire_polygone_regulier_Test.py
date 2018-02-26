from Perimetre_et_aire_polygone_regulier import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
((3),"5.2 1.3"),\
((4),"5.66 2.0"),\
((5),"5.88 2.38"),\
((6),"6.0 2.6"),\
((20),"6.26 3.09"),\
((100),"6.28 3.14")\
]


#message d'aide si besoin
help="Attention de ne pas oublier de calculer le périmètre avant l'aire. N'oublie pas non plus d'utiliser print(perimetre,aire) pour afficher le resultat."



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    send_msg("Tests validés","On pourra remarquer que plus le nombre de cotés du polygone augmente, plus le périmètre et l'aire se rapprochent des valeurs pour un cercle")
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
