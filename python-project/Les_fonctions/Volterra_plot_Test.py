#Ne pas oublier de changer le module à importer
from Volterra_plot import u,v
import matplotlib.pyplot as plt
from functools import lru_cache
import sys
import io

#On mémoize sinon c'est trop long
u=lru_cache(maxsize=None)(u)
v=lru_cache(maxsize=None)(v)

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
      l_n=list(range(0,300))
      u_n=[u(n)  for n in l_n]
      v_n=[v(n) for n in l_n]
      plt.plot(l_n,u_n, '.', l_n,v_n, '.')
      plt.title('Evolution des populations de proies et prédateurs')
      plt.show()
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
