import matplotlib.pyplot as plt
import numpy as np
from math import *

abscisses = np.linspace(-4,4,100)
ordonnées = [cos(x)+3*sin(2*x) for x in abscisses]
plt.plot(abscisses,ordonnées)
plt.show()
