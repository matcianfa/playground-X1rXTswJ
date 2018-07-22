#Ne pas oublier de changer le module à importer
import matplotlib
matplotlib.use('agg')
import sys
import io
import matplotlib.pyplot as plt
import numpy as np
#message d'aide si besoin
help=""



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> open -s /project/target/ index.html")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      fig=plt.figure()
      import plot7
      fig.savefig('output.png', dpi=fig.dpi)
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
