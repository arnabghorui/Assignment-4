import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.exp(-x**2/2) * np.sqrt(2/np.pi)

N = 10**5
x = 4 * np.random.rand(N)
y = np.random.rand(N)

y_good = y[y < f(x)]
x_good = x[y < f(x)]

t = np.linspace(0, 4, 100)
w = f(t)

plt.hist(x_good, range = (0, 4), bins = 100, density = True, label = "Histogram")
plt.plot(t, w, color = 'r', label = "PDF")
plt.xlabel("x")
plt.ylabel("PDF")
plt.legend()
plt.show()