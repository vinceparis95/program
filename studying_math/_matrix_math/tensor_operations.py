import numpy as np


# a scalar
scalar = [2]

# a vector
vector = [[1,2,3]]

# the transposed vector
trvector = np.transpose(vector)

# dot products
print(np.dot(scalar,vector))
print(np.dot(vector,trvector))