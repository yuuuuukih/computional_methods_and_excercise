import numpy as np
from .calc_mat import calc_mat


def get_QR(A):
    n = len(A)

    if len(A[0]) != n:
        print('Dimension Error!')
        return

    R = A.copy()
    Q_trans = np.identity(n)
    H = np.array([])

    for k in range(n-1): # x-yのノルムが0にならないようにn-1まで
        n_k = n - k
        x = R.T[k][k:]
        y = np.zeros(n_k)
        y[0] = np.linalg.norm(x, ord=2)

        u = (x - y) / np.linalg.norm(x - y, ord=2)

        new_H = np.identity(n)
        for i in range(k, n):
            for j in range(k, n):
                new_H[i][j] -= 2 * u[i-k] * u[j-k]
        H = np.append(H, new_H).reshape(k+1, n, n) # reshape(z, i, j)

        Q_trans = calc_mat(H[k], Q_trans)
        R = calc_mat(Q_trans, A)

    Q = Q_trans.T

    return Q, R


# 参考文献:
# https://168iroha.net/blog/topic/?id=201911251209&sorting=post_date
# https://cattech-lab.com/science-tools/lecture-mini-qr-decomposition/