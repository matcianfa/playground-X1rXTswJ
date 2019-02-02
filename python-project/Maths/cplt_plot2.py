import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 10)
y = 2*x**2+3*x-4

plt.plot(x,y,"o",color=(0.1,0.4,0.6),label="Courbe n°1",linestyle="--",linewidth=3,markeredgecolor=(1,0,0),markerfacecolor=(0,1,0), markersize=10)
plt.legend()
plt.show()
