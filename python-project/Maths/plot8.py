import matplotlib.pyplot as plt
import numpy as np
from random import *

liste =[randint(1,6)+randint(1,6) for _ in range(1000)]
plt.hist(liste,11)

plt.show()
