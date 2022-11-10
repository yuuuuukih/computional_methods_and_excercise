import numpy as np
from function.calc_mat_vec import calc_mat_vec

A = np.array([[12, 1, 5, 1, 1, 2, -4, 1, 2],
              [1, 16, -1, -4, -5, -2, 1, 2, 3],
              [5, -1, 15, -5, 3, 1, -2, 1, -4],
              [1, -4, -5, 10, 3, -3, -1, 4, 1],
              [1, -5, 3, 3, 11, -1, 4, 1, 1],
              [2, -2, 1, -3, -1, 15, -5, 2, 5],
              [-4, 1, -2, -1, 4, -5, 15, 4, -4],
              [1, 2, 1, 4, 1, 2, 4, 11, -1],
              [2, 3, -4, 1, 1, 5, -4, -1, 15]], dtype=np.float64)

alpha1 = np.ones(9, dtype=np.float64)
alpha2 = np.full(9, 1e+10, dtype=np.float64)
alpha3 = np.full(9, 1e-10, dtype=np.float64)

b1 = calc_mat_vec(A, alpha1)
b2 = calc_mat_vec(A, alpha2)
b3 = calc_mat_vec(A, alpha3)