# Since the first part is also to find a volume of unit sphere in 2 dimensions,
# I will write a common code for general d dimensions
import numpy as np
d = int(input("Enter the sphere's dimension: "))
N = 10**7

pts = np.random.random((N, d))# Random points in a unit d dimensional square box
# print(pts)
index = (pts**2).sum(axis=1)  <= 1.0
count = index.sum() # This is total number of points inside hyper sphere
volume = (count / N) * (2**d) # Multiplying volume of a hyperoctant with total numbers of hyperoctant

print("Volume of the ", d, " dimensional sphere is: ", volume)