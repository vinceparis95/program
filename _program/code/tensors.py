import numpy as np

# a scalar
scalar = [2]

# a vector
vector = [[1,2,3]]

# a matrix
matrix = [[1,2,3],
          [1,2,3],
          [1,2,3]]

# a transposed matrix
trvector = np.transpose(vector)

print(np.dot(scalar,vector))
print(np.dot(vector,trvector))