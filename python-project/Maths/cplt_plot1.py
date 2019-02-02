import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 10)
y = 2*x**2+3*x-4

plt.plot(x,y,"ro--")
plt.show()
