import numpy as np

# AをLU分解する
def get_LU(A):
    n = len(A)
    # 正方行列のチェック
    if len(A[0]) != n:
        print('Input matrix is not a square matrix!')
        return
    # Lは単位行列、Uは零行列で初期化
    L = np.identity(n, dtype=np.float64)
    U = np.zeros((n, n), dtype=np.float64)

    # 第j列目の計算
    for j in range(n):
        # 第i行目の計算
        for i in range(n):
            if i > j:
                # l_ijの計算
                L[i][j] = A[i][j]
                for k in range(j):
                    L[i][j] -= L[i][k] * U[k][j]
                # try:
                #     L[i][j] /= U[j][j]
                # except RuntimeWarning:
                #     L[i][j] = 0

                if U[j][j] < 1e-10:
                    L[i][j] = 0
                else:
                    L[i][j] /= U[j][j]

            else:
                # u_ijの計算
                U[i][j] = A[i][j]
                for k in range(i):
                    U[i][j] -= L[i][k] * U[k][j]

            i += 1
        j += 1

    return L, U