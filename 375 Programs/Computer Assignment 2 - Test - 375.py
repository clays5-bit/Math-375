import numpy as np
import Matrix_Its as mi
import pandas as pd
import matplotlib.pyplot as plt

matrix_rand = np.random.randint(0, 100, size=(20,20))
tol = .0005

matrix_j, data_j = mi.jacobian(matrix_rand, .05, tol)
matrix_gs, data_gs = mi.gauss_seidel(matrix_rand, .05, tol)

print(matrix_j)
print(data_j)
print(matrix_gs)
print(data_gs)
