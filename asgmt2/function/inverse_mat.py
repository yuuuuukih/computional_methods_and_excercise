import numpy as np
from .check_matrix import check_for_tringular_matrix
from .LU_decomposition import get_LU
from .calc_mat import calc_mat

# 下三角行列Lの逆行列Aを求める
# 下三角行列の逆行列は下三角行列であるという性質を用いる
def get_inverse_matrix_lower(L):
    check_for_tringular_matrix(L)
    n = len(L)
    A = np.zeros((n ,n))

    for j in range(n):
        for i in range(j, n):
            if i == j:
                A[i][j] = 1 / L[i][j]
            else:
                A[i][j] = -sum([L[i][k] * A[k][j] for k in range(i)]) / L[i][i]
            i += 1
        j += 1

    return A

# 上三角行列Uの逆行列を求める
def get_inverse_matrix_upper(U):
    check_for_tringular_matrix(U, 0)

    inv_U_trans = get_inverse_matrix_lower(U.T)
    return inv_U_trans.T

def get_inverse_matrix(A):
    L, U = get_LU(A)
    return calc_mat(get_inverse_matrix_upper(U), get_inverse_matrix_lower(L))