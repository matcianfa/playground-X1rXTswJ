import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)
y = 2*x**2+3*x-4

plt.plot(x,y,label="Courbe n°1")

plt.xlim(-3, 3)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks(np.linspace(-6, 12, 13))
plt.xlabel("axe des abscisses")
plt.ylabel("axe des ordonnées")
plt.grid()
plt.legend(loc='upper center')
plt.title("Ma jolie courbe")
plt.show()
