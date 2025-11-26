import numpy as np
import Matrix_Iteratives as mi
import matplotlib.pyplot as plt


matrix1_csv = "matrix1.csv"
matrix2_csv = "matrix2.csv"
tol = .005

#matrix_rand = np.random.randint(0, 100, size=(20,20))
matrix1 = np.loadtxt(matrix1_csv, delimiter=',')
#matrix2 = np.loadtxt(matrix2_csv, delimiter=',')

soln_matrix1_1 = mi.jacobi(matrix1, .001, tol)
soln_matrix1_2 = mi.jacobi(matrix1, .02, tol)

print(np.array_equal(soln_matrix1_1, soln_matrix1_2))

figs, axs = plt.subplots(nrows=2, ncols=2, figsize = (8, 8))
axs[0,0].imshow(matrix1, cmap = 'gray')
plt.axis('off')
axs[0,1].imshow(soln_matrix1_1, cmap = 'gray')
plt.axis('off')
axs[1,0].imshow(soln_matrix1_2, cmap = 'gray')
plt.axis('off')
#axs[0,1].imshow(soln_matrix3, cmap = 'gray')
#plt.axis('off')
plt.tight_layout()
plt.show()