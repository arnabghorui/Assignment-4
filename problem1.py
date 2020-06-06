import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

start = timer()
a = 1103515245
c = 12345
m = 2**31
x = 1

n = 10000
result = []
for i in range(n):
	x = (a*x + c) % m
	result.append(x/(m))

end = timer()
print("Time required: ", end - start)

plt.hist(result, density = True)
plt.show()
