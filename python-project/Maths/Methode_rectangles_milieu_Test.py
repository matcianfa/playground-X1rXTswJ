#Ne pas oublier de changer le module à importer
from Methode_rectangles import mon_programme
from math import *
import sys
import io


#liste des couples input/output
input_output=[\
((lambda x:x,0,4,1000),8.,"x"),\
((lambda x:x**2,0,4,1000),64/3,"x²"),\
((lambda x:sqrt(1-x**2),-1,1,1000),pi/2,"racine(1-x²) (C'est un demi cercle de rayon 1 donc on est censé trouver pi/2)"),\
((lambda x:exp(-x**2/2)/sqrt(2*pi),-1,1,1000),0.6827,"exp(-x²/2) (C'est la courbe de Gauss)"),\
((lambda x:x*(1-x)*(sin(200*x*(1-x)))**2,0,1,1000),0.080498,"x(1-x)sin²(200*x*(1-x))")\
]


#message d'aide si besoin
help=""



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> open -s /project/target/ Maths/Monte_carlo.html")
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp,txt in input_output:
        count1=mon_programme(*inp)
        assert abs(count1-outp)<0.001, "En testant les valeurs f(x)={}, a={}, b={} et n={} le résultat obtenu est {} au lieu de {}".format(str(txt),str(inp[1]),str(inp[2]),str(inp[3]),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs f(x)={}, a={}, b={} et n={}, votre résultat est {} et la valeur réelle est {}".format(str(txt),str(inp[1]),str(inp[2]),str(inp[3]),str(count1),str(outp)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
