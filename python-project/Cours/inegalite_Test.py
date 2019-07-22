import Classe
from Classe import Fraction

valeurs_a_tester = [["Fraction(1,3)<Fraction(1,2)","True"],["Fraction(2,3)<Fraction(1,2)","False"],["Fraction(1,3)<=Fraction(1,2)","True"],["Fraction(2,4)<=Fraction(1,2)","True"],["Fraction(1,3)>Fraction(1,2)","False"],["Fraction(2,3)>=Fraction(1,2)","True"]]

# Fonction qui permet d'envoyer un message sur le channel    
def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))
    
#--------------------------------------
def test():
    try:
        for valeur,sol in valeurs_a_tester:
            assert sol == str(eval(valeur)), "En testant  '{}' le résultat obtenu est {} au lieu de {}".format(valeur,str(eval(valeur)),str(sol))
            send_msg("Tests validés","En testant les valeurs '{}' le résultat obtenu est bien {}".format(valeur,str(sol)))
        print("TECHIO> success true")
    except AssertionError as e:
        print("TECHIO> success false")
        send_msg("Oops! ", e)
        

#--------------------------------------
if __name__ == "__main__": test()
