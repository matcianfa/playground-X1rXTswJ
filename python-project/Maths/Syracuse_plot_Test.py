#Ne pas oublier de changer le module à importer
from Syracuse_plot import syracuse,N
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import sys
import io



#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> open -s /project/target/ index.html")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      u_n=syracuse(N)
      l_n=list(range(len(u_n)))
      fig=plt.figure()
      plt.plot(l_n,u_n, '.')
      plt.title('Suite de Syracuse pour N='+N)
      fig.savefig('output.png', dpi=fig.dpi)
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
