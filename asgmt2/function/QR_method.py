import numpy as np
from .QR_decomposition import get_QR
from .calc_mat import calc_mat

def get_mu_by_wilkinson_shift(A):
    a11 = A[-2][-2]
    a12 = A[-2][-1]
    a21 = A[-1][-2]
    a22 = A[-1][-1]

    b = a11 + a22
    c = a11 * a22 - a12 * a21

    lamb1 = (b + np.sqrt(b**2 - 4 * c)) / 2
    lamb2 = (b - np.sqrt(b**2 - 4 * c)) / 2
    # lamb1 = (b + np.sqrt(np.abs(b**2 - 4 * c))) / 2
    # lamb2 = (b - np.sqrt(np.abs(b**2 - 4 * c))) / 2

    mu = lamb1 if np.abs(lamb1 - a22) < np.abs(lamb2 - a22) else lamb2
    return mu

def get_eigen_value_by_QR(A0, EPS=1e-5, iter_max=1000):
    n = len(A0)
    # 正方行列のチェック
    if len(A0[0]) != n:
        print('Input matrix is not a square matrix!')
        return

    eigen_value = np.array([])
    A = A0
    for k in range(n-1):
        dim_A = n - k
        # deflation
        new_A = np.zeros((dim_A, dim_A))
        for i in range(dim_A):
            for j in range(dim_A):
                new_A[i][j] = A[i][j]
        A = new_A

        for i in range(iter_max):
            mu = get_mu_by_wilkinson_shift(A)
            Q, R = get_QR(A - mu * np.identity(dim_A))
            A = calc_mat(R, Q) + mu * np.identity(dim_A)

            if np.abs(A[-1][-2]) < EPS:
                # print(A[-1][-1])
                eigen_value = np.append(eigen_value, A[-1][-1])

                if k == n-2:
                    eigen_value = np.append(eigen_value, A[0][0])
                break

    return eigen_value

# 参考文献：
# https://cattech-lab.com/science-tools/lecture-mini-eigenvalue-qr1/
# https://168iroha.net/blog/topic/?id=201911251209&sorting=post_date