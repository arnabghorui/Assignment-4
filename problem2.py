import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

start = timer()
n = 10000
result = []
for i in range(n):
	result.append( np.random.rand() )

end = timer()
print("Time required: ", end - start)

plt.hist(result, density = True)
plt.show()