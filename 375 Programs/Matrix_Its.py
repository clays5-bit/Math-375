import numpy as np
import pandas as pd

def spd_check(matrix):
    matrix
    eigenvalues, eigenvector = np.linalg.eig(matrix)
    if np.array_equal(matrix, matrix.T) and all(number > 0 for number in eigenvalues):
        print("SPD")
        return True
    else:
        print("Not SPD")
        return False

def rx(matrix):
    matrix_size = matrix.shape
    if matrix_size[0] == matrix_size[1]:
        xp = np.pad(matrix, 1, mode="constant", constant_values=0)
        x1 = xp[0:-2, 1:-1] #shift down
        x2 = xp[2: , 1:-1] #shift up
        x3 = xp[1:-1, 0:-2] #shift left
        x4 = xp[1:-1, 2: ] # shift right
        x5 = xp[1:-1, 1:-1] # center
        xS = x1 + x2 + x3 + x4
        rx_matrices = [xS, x1, x2, x3, x4, x5] 
        return rx_matrices
    else:
        print("Matrix is not square")

def jacobian(matrix, lamb, tol):
    rx_matrix = rx(matrix)
    matrix_soln1 = (1/(1+4*lamb))*(matrix + lamb*(rx_matrix[0]))
    residual = np.linalg.norm(matrix_soln1-matrix)
    n = 0 
    data = [residual]
    while residual > tol and n < 100:
        rx_matrix = rx(matrix_soln1)
        matrix_soln2 = (1/(1+4*lamb))*(matrix + lamb*(rx_matrix[0]))
        residual = np.linalg.norm(matrix_soln2-matrix_soln1)
        matrix_soln1 = matrix_soln2.copy()
        n += 1
        data.append(residual)
    data = pd.DataFrame(data)
    return matrix_soln1, data

def gauss_seidel(matrix, lamb, tol):
    matrix_soln2 = matrix.copy()
    matrix_dim = matrix.shape
    residual = tol + 1
    n = 0
    data = []
    while residual > tol and n < 100:
        matrix_soln1 = matrix_soln2.copy()
        for i in range(matrix_dim[0]):
            for j in range(matrix_dim[1]):
                x1 = matrix_soln2[i-1, j] if i > 0 else 0
                x2 = matrix_soln2[i, j-1] if j > 0 else 0
                x3 = matrix_soln1[i+1, j] if i+1 < matrix_dim[0] else 0
                x4 = matrix_soln1[i, j+1] if j+1 < matrix_dim[1] else 0
                matrix_soln2[i,j] = (1/(1+lamb*4))*(matrix[i,j]+lamb*(x1+x2+x3+x4))
        residual = np.linalg.norm(matrix_soln2-matrix_soln1)
        n += 1
        data.append(residual)
    data = pd.DataFrame(data)
    return matrix_soln2, data