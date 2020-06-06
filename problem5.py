import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.rand(10000)
x2 = np.random.rand(10000)

y1 = np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)
y2 = np.sqrt(-2*np.log(x1)) * np.sin(2*np.pi*x2)

plt.hist(y1, bins = 100, range = (-5,5), density = True, label = "Density histogram")

x = np.linspace(-5,5,100)
y = np.exp(-x**2/2) / np.sqrt(2*np.pi)
plt.plot(x, y, label = "Gaussian PDF")
plt.xlabel("x")
plt.legend()
plt.grid(True)
plt.show()