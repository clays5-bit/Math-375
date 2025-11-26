import numpy as np
import Matrix_Its as mi
import pandas as pd
import matplotlib.pyplot as plt

matrix1_csv = "matrix1.csv"
matrix2_csv = "matrix2.csv"
tol = .0005

matrix_rand = np.random.randint(0, 100, size=(20,20))
matrix1 = np.loadtxt(matrix1_csv, delimiter=',')
matrix2 = np.loadtxt(matrix2_csv, delimiter=',')

#matrix_solnJ1_1 = mi.jacobian(matrix1, .6, tol)
#matrix_solnJ1_2 = mi.jacobian(matrix1, 1, tol)
#matrix_solnJ1_3 = mi.jacobian(matrix1, 1.4, tol)

#matrix_solnJ2_1 = mi.jacobian(matrix2, .6, tol)
#matrix_solnJ2_2 = mi.jacobian(matrix2, 1, tol)
#matrix_solnJ2_3 = mi.jacobian(matrix2, 1.4, tol)

#matrix_solnG1_1 = mi.gauss_seidel(matrix1, .6, tol)
#matrix_solnG1_2 = mi.gauss_seidel(matrix1, 1, tol)
#matrix_solnG1_3 = mi.gauss_seidel(matrix1, 1.4, tol)

matrix_solnG2_1 = mi.gauss_seidel(matrix2, .6, tol)
matrix_solnG2_2 = mi.gauss_seidel(matrix2, 1, tol)
matrix_solnG2_3 = mi.gauss_seidel(matrix2, 1.4, tol)

pfigs, axs = plt.subplots(nrows=1, ncols=4, figsize = (8, 8))
#Jacobian, CSV1
#axs[0].imshow(matrix1, cmap = 'gray')
#plt.axis('off')
#axs[1].imshow(matrix_solnJ1_1, cmap = 'gray')
#plt.axis('off')
#axs[2].imshow(matrix_solnJ1_2, cmap = 'gray')
#plt.axis('off')
#axs[3].imshow(matrix_solnJ1_3, cmap = 'gray')
#plt.axis('off')

#Jacobian, CSV2
#axs[0].imshow(matrix1, cmap = 'gray')
#plt.axis('off')
#axs[1].imshow(matrix_solnJ2_1, cmap = 'gray')
#plt.axis('off')
#axs[2].imshow(matrix_solnJ2_2, cmap = 'gray')
#plt.axis('off')
#axs[3].imshow(matrix_solnJ2_3, cmap = 'gray')
#plt.axis('off')

#Gauss-Seidel, CSV1
#axs[0].imshow(matrix1, cmap = 'gray')
#plt.axis('off')
#axs[1].imshow(matrix_solnG1_1, cmap = 'gray')
#plt.axis('off')
#axs[2].imshow(matrix_solnG1_2, cmap = 'gray')
#plt.axis('off')
#axs[3].imshow(matrix_solnG1_3, cmap = 'gray')
#plt.axis('off')

#Gauss-Seidel, CSV2
axs[0].imshow(matrix2, cmap = 'gray')
plt.axis('off')
axs[1].imshow(matrix_solnG2_1, cmap = 'gray')
plt.axis('off')
axs[2].imshow(matrix_solnG2_2, cmap = 'gray')
plt.axis('off')
axs[3].imshow(matrix_solnG2_3, cmap = 'gray')
plt.axis('off')

plt.tight_layout()
plt.show()