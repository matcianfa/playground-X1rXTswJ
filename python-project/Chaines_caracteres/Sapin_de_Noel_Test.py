#Ne pas oublier de changer le module à importer
from Sapin_de_Noel import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
(2,".^. ^^^"),\
(3,"..^.. .^^^. ^^^^^"),\
(4,"...^... ..^^^.. .^^^^^. ^^^^^^^"),\
(1,"^"),\
(20,"...................^................... ..................^^^.................. .................^^^^^................. ................^^^^^^^................ ...............^^^^^^^^^............... ..............^^^^^^^^^^^.............. .............^^^^^^^^^^^^^............. ............^^^^^^^^^^^^^^^............ ...........^^^^^^^^^^^^^^^^^........... ..........^^^^^^^^^^^^^^^^^^^.......... .........^^^^^^^^^^^^^^^^^^^^^......... ........^^^^^^^^^^^^^^^^^^^^^^^........ .......^^^^^^^^^^^^^^^^^^^^^^^^^....... ......^^^^^^^^^^^^^^^^^^^^^^^^^^^...... .....^^^^^^^^^^^^^^^^^^^^^^^^^^^^^..... ....^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^.... ...^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^... ..^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^.. .^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")\
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
      for inp,outp_l in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(inp)
        reponse = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        send_msg("Tests validés","Pour n="+str(inp))
        for count1,outp in zip(reponse.split("\n"),outp_l.split()):
          assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
          send_msg("Tests validés","{}".format(str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
