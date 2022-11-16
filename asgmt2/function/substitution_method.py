import numpy as np
from .check_matrix import check_for_tringular_matrix
from .check_matrix import Ab_error_check


# 下三角行列Lをとって前進代入法で解く
def calc_forward(L, b):
    n = len(L)
    Ab_error_check(L, b)

    # Aが下三角行列か否かのチェック
    check_for_tringular_matrix(L)

    x = np.zeros(n)

    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= L[i][j] * x[j]
        x[i] /= L[i][i]

    return x

# 上三角行列Uをとって後退代入法で解く
def calc_backward(U, b):
    n = len(U)
    Ab_error_check(U, b)

    # 上三角行列のチェック
    check_for_tringular_matrix(U, 0)

    x = np.zeros(n)
    for k in range(n):
        i = n-k-1
        x[i] = b[i]
        for j in range(k):
            x[i] -= U[i][n-j-1] * x[n-j-1]
        x[i] /= U[i][i]

    return x

# L,Uを受け取って前進代入と後退代入で求める
def calc_forward_backward_by_LU(L, U, b):
    y = calc_forward(L, b)
    x = calc_backward(U, y)

    return x