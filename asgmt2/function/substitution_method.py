import numpy as np
from .check_matrix import check_for_tringular_matrix

def basic_error_check(A, b):
    n = len(A)
    if len(b) != n:
        print('Dimention Error!')
        return

# 下三角行列Lをとって前進代入法で解く
def calc_forward(L, b):
    n = len(L)
    basic_error_check(L, b)

    # Aが下三角行列か否かのチェック
    check_for_tringular_matrix(L)

    x = np.zeros(n)

    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= L[i][j] * x[j]
            j += 1
        x[i] /= L[i][i]
        i += 1

    return x

# 上三角行列Uをとって後退代入法で解く
def calc_backward(U, b):
    n = len(U)
    basic_error_check(U, b)

    # 上三角行列のチェック
    check_for_tringular_matrix(U, 0)

    x = np.zeros(n)
    for k in range(n):
        i = n-k-1
        x[i] = b[i]
        for j in range(k):
            x[i] -= U[i][n-j-1] * x[n-j-1]
            j += 1
        x[i] /= U[i][i]
        k += 1

    return x