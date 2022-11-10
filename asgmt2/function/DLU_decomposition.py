import numpy as np

def get_DLU(A):
    n = len(A)
    # 正方行列のチェック
    if len(A[0]) != n:
        print('Input matrix is not a square matrix!')
        return

    D = np.zeros((n, n))
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    # D生成
    for i in range(n):
        D[i][i] = A[i][i]
        i += 1

    # L生成
    for i in range(1, n):
        for j in range(i):
            L[i][j] = A[i][j]
            j += 1
        i += 1

    # U生成
    for i in range(n-1):
        for j in range(i+1, n):
            U[i][j] = A[i][j]
            j += 1
        i += 1

    return D, L, U
