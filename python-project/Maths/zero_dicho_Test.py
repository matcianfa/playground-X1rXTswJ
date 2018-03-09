#Ne pas oublier de changer le module à importer
from zero_dicho import mon_programme
from math import *
import sys
import io


#liste des couples input/output
input_output=[\
(((lambda x: 4*x+3),-2,0),-0.75,"4*x+3"),\
(((lambda x : x**2-5*x+6),0,2.5),2,"x**2-5*x+6"),\
(((lambda x : x**2-x-1),1,20),(1+sqrt(5))/2,"x**2-x-1"),\
(((lambda x : tan(x)-x),4,5),4.493409734469959,"tan(x)-x")\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser return pour afficher le resultat"



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
        assert abs(count1-outp)<=0.000001, "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant f(x)={}, a={} et b={} le résultat obtenu est {} et la valeur du zéro est {}".format(txt,str(inp[1]),str(inp[2]),str(count1),str(outp)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
