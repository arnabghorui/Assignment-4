import matplotlib.pyplot as plt
import numpy as np

y_data = np.loadtxt("problem4.txt")

x_ana = np.linspace(0,5,51)
y_ana = 2*np.exp(-2*x_ana)

plt.hist(y_data, bins = 50, range = (0,5), density = True, label = "Density histogram")
plt.plot(x_ana, y_ana,  label = "Exponential PDF(mean = 0.5)")
plt.xlabel("x")
plt.legend()
plt.grid(True)
plt.show()