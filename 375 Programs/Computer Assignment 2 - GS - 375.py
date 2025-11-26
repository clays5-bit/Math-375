import numpy as np
import Matrix_Its as mi
import pandas as pd
import matplotlib.pyplot as plt

matrix1_csv = r"C:\Users\clays\Documents\GitHub\Math-375\375 Programs\matrix1.csv"
matrix2_csv = r"C:\Users\clays\Documents\GitHub\Math-375\375 Programs\matrix2.csv"
#matrix1_csv = "matrix1.csv"
#matrix2_csv = "matrix2.csv"
tol = .0005

matrix1 = np.loadtxt(matrix1_csv, delimiter=',')
matrix2 = np.loadtxt(matrix2_csv, delimiter=',')

matrix_solnG1_1, dataG1_1 = mi.gauss_seidel(matrix1, .5, tol)
matrix_solnG1_2, dataG1_2 = mi.gauss_seidel(matrix1, 1, tol)
matrix_solnG1_3, dataG1_3 = mi.gauss_seidel(matrix1, 1.5, tol)

matrix_solnG2_1, dataG2_1 = mi.gauss_seidel(matrix2, .5, tol)
matrix_solnG2_2, dataG2_2 = mi.gauss_seidel(matrix2, 1, tol)
matrix_solnG2_3, dataG2_2 = mi.gauss_seidel(matrix2, 1.5, tol)

pfigs, axs = plt.subplots(nrows=2, ncols=4, figsize = (8, 8))

#Gauss-Seidel, CSV1
axs[0,0].imshow(matrix1, cmap = 'gray')
axs[0,0].axis('off')
axs[0,1].imshow(matrix_solnG1_1, cmap = 'gray')
axs[0,1].axis('off')
axs[0,2].imshow(matrix_solnG1_2, cmap = 'gray')
axs[0,2].axis('off')
axs[0,3].imshow(matrix_solnG1_3, cmap = 'gray')
axs[0,3].axis('off')

#Gauss-Seidel, CSV2
axs[1,0].imshow(matrix2, cmap = 'gray')
axs[1,0].axis('off')
axs[1,1].imshow(matrix_solnG2_1, cmap = 'gray')
axs[1,1].axis('off')
axs[1,2].imshow(matrix_solnG2_2, cmap = 'gray')
axs[1,2].axis('off')
axs[1,3].imshow(matrix_solnG2_3, cmap = 'gray')
axs[1,3].axis('off')

plt.tight_layout()
plt.show()