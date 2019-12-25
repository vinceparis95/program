import numpy as np

# a scalar
scalar = [2]

# a vector
vector = [[1,2,3]]

# a matrix
matrix = [[1,2,3],
          [1,2,3],
          [1,2,3]]

# a tensor
tensor = [[[1,2,3],
          [1,2,3],
          [1,2,3]],
          [[1,2,3],
          [1,2,3],
          [1,2,3]]]

# a transposed matrix
trvector = np.transpose(vector)

print(vector, "\n", trvector)