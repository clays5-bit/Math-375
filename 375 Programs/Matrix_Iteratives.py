import numpy as np

#checks if the matrix is strictly diagonally dominant
def sdd_check(matrix):
    matrix_size = matrix.shape
    diags = []
    for n in range(matrix_size[0]):
        diags.append(float(matrix[n,n]))
    row_sums = np.sum(matrix, axis=1)
    for n in range(len(diags)):
        if diags[n] <= row_sums[n]-diags[n]:
            print("Not SDD")
            return(False)
    return(True)

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
        x1 = xp[0:-2, 1:-1]
        x2 = xp[2: , 1:-1]
        x3 = xp[1:-1, 0:-2]
        x4 = xp[1:-1, 2: ]
        x5 = xp[1:-1, 1:-1]
        rx = x1 + x2 + x3 + x4 - 4*x5
        return rx
    else:
        print("Matrix is not square")

def jacobi(matrix, lambduh, tol):
    soln_matrix1 = matrix
    for n in range(100):
        print(n)
        rx_matrix = rx(soln_matrix1)
        soln_matrix2 = soln_matrix1 + lambduh*rx_matrix
        residual = np.linalg.norm(soln_matrix2-soln_matrix1)
        print(residual)
        if residual < tol:
            return soln_matrix2
        soln_matrix1 = soln_matrix2
    return soln_matrix2
