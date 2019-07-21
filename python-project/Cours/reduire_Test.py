import Classe
from Classe import Fraction

valeurs_a_tester = [["str(Fraction(1,2).reduire())","1 / 2"],["str(Fraction(4,12).reduire())","1 / 3"],["str(Fraction(12,3).reduire())","4 / 1"]]

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
