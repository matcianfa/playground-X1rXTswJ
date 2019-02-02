import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)
y = 2*x**2+3*x-4

plt.plot(x,y)
plt.ylim(-8,11)

plt.annotate(r"Le minimum atteint en $-\frac{b}{2a}$", xy=(-3/4, -41/8),xytext=(0, -5.5), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-.4"))
plt.annotate("Annotation 1",xy=(0,0),xytext=(-1,3))

plt.show()
