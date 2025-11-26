import numpy as np
import Matrix_Its as mi
import pandas as pd
import matplotlib.pyplot as plt

#matrix1_csv = r"C:\Users\Sean's Desktop\Documents\GitHub\Math-375\375 Programs\matrix1.csv"
#matrix2_csv = r"C:\Users\Sean's Desktop\Documents\GitHub\Math-375\375 Programs\matrix2.csv"
matrix1_csv = "matrix1.csv"
matrix2_csv = "matrix2.csv"
tol = .005

matrix1 = np.loadtxt(matrix1_csv, delimiter=',')
matrix2 = np.loadtxt(matrix2_csv, delimiter=',')

matrix_solnJ1_1, dataJ1_1 = mi.jacobian(matrix1, .5, tol)
matrix_solnJ1_2, dataJ1_2 = mi.jacobian(matrix1, 1, tol)
matrix_solnJ1_3, dataJ1_3 = mi.jacobian(matrix1, 1.5, tol)

matrix_solnJ2_1, dataJ2_1 = mi.jacobian(matrix2, .5, tol)
matrix_solnJ2_2, dataJ2_2 = mi.jacobian(matrix2, 1, tol)
matrix_solnJ2_3, dataJ2_3 = mi.jacobian(matrix2, 1.5, tol)

pfigs, axs = plt.subplots(nrows=2, ncols=4, figsize = (8, 8))
#Jacobian, CSV1
axs[0,0].imshow(matrix1, cmap = 'gray')
axs[0,0].axis('off')
axs[0,1].imshow(matrix_solnJ1_1, cmap = 'gray')
axs[0,1].axis('off')
axs[0,2].imshow(matrix_solnJ1_2, cmap = 'gray')
axs[0,2].axis('off')
axs[0,3].imshow(matrix_solnJ1_3, cmap = 'gray')
axs[0,3].axis('off')

#Jacobian, CSV2
axs[1,0].imshow(matrix2, cmap = 'gray')
axs[1,0].axis('off')
axs[1,1].imshow(matrix_solnJ2_1, cmap = 'gray')
axs[1,1].axis('off')
axs[1,2].imshow(matrix_solnJ2_2, cmap = 'gray')
axs[1,2].axis('off')
axs[1,3].imshow(matrix_solnJ2_3, cmap = 'gray')
axs[1,3].axis('off')

plt.tight_layout()
plt.show()