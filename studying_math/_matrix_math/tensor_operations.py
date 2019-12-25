import numpy as np


# a scalar
scalar = [2]

# a row vector
vector = [[1, 2, 3]]

# the transposed vector
trvector = np.transpose(vector)

# dot products
print(np.dot(scalar, vector))
print(np.dot(vector, trvector))

# kron, outer product, and multiply
print(np.kron(vector, trvector))
print(np.outer(vector,trvector))
print(np.multiply(vector,trvector))

