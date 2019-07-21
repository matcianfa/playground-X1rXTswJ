import Classe
from Classe import Fraction

valeurs_a_tester = [["str(Fraction(1,-2))","-1 / 2"],["str(Fraction(4,3))","4 / 3"],["str(Fraction(-4,3))","-4 / 3"],["str(Fraction(-4,-3))","4 / 3"]]

# Fonction qui permet d'envoyer un message sur le channel    
def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))
    
#--------------------------------------
def test():
    try:
        for valeur,sol in valeurs_a_tester:
            assert sol == str(eval(valeur)), "En testant  '{}' le résultat obtenu est {} au lieu de {}".format(valeur,str(eval(valeur)),str(sol))
            send_msg("Tests validés","En testant les valeurs '{}' le résultat obtenu est bien {}".format(valeur,str(sol)))
        try :
            Fraction(1,0)
            assert false, "Pas d'erreur lorsqu'on divise par 0 !"
        except ZeroDivisionError :
            send_msg("Tests validés","En testant les valeurs 'Fraction(1,0)', l'erreur ZeroDivisionError est bien levée)
        print("TECHIO> success true")
    except AssertionError as e:
        print("TECHIO> success false")
        send_msg("Oops! ", e)
        

#--------------------------------------
if __name__ == "__main__": test()
