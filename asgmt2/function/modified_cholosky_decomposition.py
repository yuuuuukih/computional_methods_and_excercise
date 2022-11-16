import numpy as np
from .check_matrix import check_for_diagonal_matrix
from .calc_mat import calc_mat

# A=LDLt
def get_LDLt(A):
    n = len(A)
    # 正方行列のチェック
    if len(A[0]) != n:
        print('Input matrix is not a square matrix!')
        return
    # Lは単位行列、Dは零行列で初期化
    L = np.identity(n)
    D = np.zeros((n, n))

    D[0][0] = A[0][0]
    for i in range(n):
        for j in range(i):
            L[i][j] = A[i][j]
            for k in range(j):
                L[i][j] -= L[i][k] * L[j][k] * D[k][k]
            L[i][j] /= D[j][j]
        D[i][i] = A[i][i]
        for k in range(i):
            D[i][i] -= L[i][k]**2 * D[k][k]

    return L, D

# D^1/2
def get_square_root_matrix(D):
    # 対角行列のチェック
    check_for_diagonal_matrix(D)
    n = len(D)
    sqrt_D = np.zeros((n, n))

    for k in range(n):
        sqrt_D[k][k] = np.sqrt(D[k][k])

    return sqrt_D

# A=UtU
def get_U_by_LD(A):
    L ,D = get_LDLt(A)
    U = calc_mat(get_square_root_matrix(D), L.T)

    return U

# 参考文献：
# http://www.oishi.info.waseda.ac.jp/thesis/yamamoto/1g00p013.pdf