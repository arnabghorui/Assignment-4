import numpy as np
import scipy.stats as scat

n = 144
k = 10 #Degrees of freedom
s = np.array([1,2,3,4,5,6,5,4,3,2,1])
p_s = s / 36

Y_s1 = np.array([4,10,10,13,20,18,18,11,13,14,13])
Y_s2 = np.array([3,7,11,15,19,24,21,17,13,9,5])

V_1, V_2 = 0, 0
for i in range(len(Y_s1)):
	V_1 += (Y_s1[i] - n*p_s[i])**2 / (n*p_s[i])
	V_2 += (Y_s2[i] - n*p_s[i])**2 / (n*p_s[i])

P = np.array([0.0, 0.0])
P[0], P[1] = 1-scat.chi2.cdf(V_1, k), 1-scat.chi2.cdf(V_2, k)

for i in [0,1]:
	print("For part ", i+1, ":")
	print("V = ", V_1, ", P(V > v) = ", P[i])
	if P[i]<0.01 or P[i]>0.99:
		print("Not sufficiently random\n")
	elif 0.01<=P[i]<0.05 or 0.95<P[i]<=0.99:
		print("Suspect\n")
	elif 0.05<=P[i]<0.1 or 0.9<P[i]<=0.95:
		print("Almost suspect\n")
	elif 0.1<=P[i]<=0.9:
		print("Sufficiently random\n")
