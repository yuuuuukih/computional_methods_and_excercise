import numpy as np

# AB=Cを計算
def calc_mat(A, B):
    if len(A[0]) != len(B):
        print('Cannot calculate!')
        return

    n = len(A)
    m = len(B[0])
    C = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            C[i][j] = sum([A[i][k] * B[k][j] for k in range(len(B))])
            j += 1
        i += 1

    return C