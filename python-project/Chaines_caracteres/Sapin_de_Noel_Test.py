#Ne pas oublier de changer le module à importer
module="Les_boucles/Sapin_de_Noel"

import sys
import io
from ma_bao import *
tester("from Sapin_de_Noel import mon_programme",globals())




#liste des couples input/output
input_output=[\
(2,".^. ^^^"),\
(3,"..^.. .^^^. ^^^^^"),\
(4,"...^... ..^^^.. .^^^^^. ^^^^^^^"),\
(1,"^"),\
(0,"."),\
(20,"...................^................... ..................^^^.................. .................^^^^^................. ................^^^^^^^................ ...............^^^^^^^^^............... ..............^^^^^^^^^^^.............. .............^^^^^^^^^^^^^............. ............^^^^^^^^^^^^^^^............ ...........^^^^^^^^^^^^^^^^^........... ..........^^^^^^^^^^^^^^^^^^^.......... .........^^^^^^^^^^^^^^^^^^^^^......... ........^^^^^^^^^^^^^^^^^^^^^^^........ .......^^^^^^^^^^^^^^^^^^^^^^^^^....... ......^^^^^^^^^^^^^^^^^^^^^^^^^^^...... .....^^^^^^^^^^^^^^^^^^^^^^^^^^^^^..... ....^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^.... ...^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^... ..^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^.. .^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")\
]


#message d'aide si besoin
help="Quand il n'y a pas de sapin, il y a quand même la neige..."



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    afficher_correction()
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
