#Ne pas oublier de changer le module à importer
from hanoi import hanoi as mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
(2,['A B', 'A C', 'B C']),\
(3,['A C', 'A B', 'C B', 'A C', 'B A', 'B C', 'A C']),\
(4,['A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C']),\
(10,['A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'C B', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'B A', 'C A', 'C B', 'A B', 'C A', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C', 'A B', 'C A', 'C B', 'A B', 'A C', 'B C', 'B A', 'C A', 'B C', 'A B', 'A C', 'B C'])\
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
        mon_programme(inp,"A","B","C")
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        send_msg("Tests validés","Pour n="+inp+" la marche à suivre est :")
        for i,rep in enumerate(count1.split("\n")):
          assert rep == outp[i], "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(rep),str(outp[i]))
          send_msg("Tests validés",str(rep))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
