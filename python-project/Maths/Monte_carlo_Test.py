#Ne pas oublier de changer le module à importer
from Monte_carlo import mon_programme
from math import *
import sys
import io


#liste des couples input/output
input_output=[\
((lambda x:x,0,4),8.,"x"),\
((lambda x:x**2,0,4),64/3,"x²"),\
((lambda x:sqrt(1-x**2),-1,1),pi/2,"racine(1-x²) (C'est un demi cercle de rayon 1 donc on est censé trouver pi/2)"),\
((lambda x:exp(-x**2/2)/sqrt(2*pi),-1,1),0.6827,"exp(-x²/2) (C'est la courbe de Gauss)"),\
((lambda x:x*(1-x)*(sin(200*x*(1-x)))**2,0,1),0.080498,"x(1-x)sin²(200*x*(1-x))")\
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
      for inp,outp,txt in input_output:
        count1=mon_programme(*inp)
        assert abs(count1-outp)<0.01, "En testant les valeurs f(x)={}, a={} et b={} le résultat obtenu est {} au lieu de {}".format(str(txt),str(inp[1]),str(inp[2]),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs f(x)={}, a={} et b={}, votre résultat est {} et la valeur réelle est {}".format(str(txt),str(inp[1]),str(inp[2]),str(count1),str(outp)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
