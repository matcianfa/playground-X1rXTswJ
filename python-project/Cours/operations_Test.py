import Classe
from Classe import Fraction

valeurs_a_tester = [["Fraction(1,3)+Fraction(1,2)","Fraction(5,6)"],["Fraction(1,2)-Fraction(1,3)","Fraction(1,6)"],["Fraction(3,4)-Fraction(1,4)","Fraction(1,2)"],["Fraction(2,3)*Fraction(1,2)","Fraction(1,3)"],["Fraction(2,3)/Fraction(4,3)","Fraction(1,2)"]]

# Fonction qui permet d'envoyer un message sur le channel    
def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))
    
#--------------------------------------
def test():
    try:
        for valeur,sol in valeurs_a_tester:
            assert eval(sol) == eval(valeur), "En testant  '{}' le résultat obtenu est {} au lieu de {}".format(valeur,str(eval(valeur)),str(sol))
            send_msg("Tests validés","En testant les valeurs '{}' le résultat obtenu est bien {}".format(valeur,str(sol)))
        print("TECHIO> success true")
    except AssertionError as e:
        print("TECHIO> success false")
        send_msg("Oops! ", e)
        

#--------------------------------------
if __name__ == "__main__": test()
