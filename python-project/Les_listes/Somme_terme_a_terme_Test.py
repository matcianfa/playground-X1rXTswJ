#Ne pas oublier de changer le module à importer
from Somme_terme_a_terme import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
(([1],[1]),[2]),\
(([1,2],[1,3]),[2,5]),\
(([1,2,3,4,1,2,3],[1,3,-1,5,8,0,1]),[2,5,2,9,9,2,4])\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    send_msg("Bonus","Astuce pour aller beaucoup plus vite, vous pourriez utiliser la fonction zip :")
    send_msg("Bonus","[a+b for a,b in zip(liste_1,liste2)]")
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
        assert str(count1) == str(outp), "En testant les valeurs '{}' le résultat obtenu est '{}' au lieu de '{}'".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs '{}' le résultat obtenu est bien '{}'".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
