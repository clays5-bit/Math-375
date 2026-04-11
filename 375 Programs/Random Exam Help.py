import numpy as np

matrix1 = np.array([[0,-8,-2],[-6,2,-9],[-8,12,0]])
matrix2 = np.array([[4, 6, 4],[-6,2,12],[-8,-3,14]])

print(np.linalg.cond(matrix1, p = np.inf))
print(np.linalg.cond(matrix2, p = np.inf))

