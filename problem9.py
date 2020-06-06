import matplotlib.pyplot as plt
import numpy as np

def f(x):
	if 3 < x < 7:
		return 1
	else:
		return 0

nsteps = 10000
theta = np.zeros(nsteps)
theta_all = np.zeros(nsteps)
theta[0] = 5

for k in range(nsteps - 1):
	theta_prime = theta[k] + np.random.standard_normal()
	theta_all[k] = theta_prime
	r = np.random.rand()

	if f(theta_prime) / f(theta[k]) > r:
		theta[k+1] = theta_prime
	else:
		theta[k+1] = theta[k]

step = np.linspace(1,nsteps, nsteps)
fig1,ax1 = plt.subplots()
plt.scatter(step,theta_all, label="All points", color = 'orange')
plt.plot(step, theta, label = "Marcov chain")
ax1.set_xlabel("step")
ax1.set_ylabel("theta")
plt.legend()
plt.title('Marcov chain')

fig2,ax2=plt.subplots()
plt.hist(theta, bins = 100, density = True)
X = np.linspace(3, 7, 100)
Y = np.ones(100) / 4
plt.plot(X,Y,'r-')
plt.title('PDF')
plt.show()


plt.show()