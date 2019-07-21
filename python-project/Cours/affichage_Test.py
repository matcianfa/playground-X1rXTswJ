import Classe
from Classe import Fraction

valeurs_a_tester = [["str(Fraction(1,2))","1 / 2"],["str(Fraction(4,3))","4 / 3"],["str(Fraction(12,12345))","12 / 12345"]]


#--------------------------------------
def test():
    try:
        for valeur,sol in valeurs_a_tester:
            assert sol == str(eval(valeur)), "En testant  '{}' le résultat obtenu est {} au lieu de {}".format(valeur,str(eval(valeur)),str(sol))
            send_msg("Tests validés","En testant les valeurs '{}' le résultat obtenu est bien {}".format(valeur,str(sol)))
        success(chemin+module)
    except AssertionError as e:
        fail()
        send_msg("Oops! ", e)
        if help:
            send_msg("Aide 💡", help)

#--------------------------------------
if __name__ == "__main__": test()
