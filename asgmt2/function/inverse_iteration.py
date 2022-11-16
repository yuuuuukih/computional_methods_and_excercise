import numpy as np
from .LU_decomposition import get_LU
from .substitution_method import calc_forward_backward_by_LU

def calc_inverse_iteration(A, lamb, EPS=1e-10, k_max=5):
    n = len(A)
    # 正方行列のチェック
    if len(A[0]) != n:
        print('Input matrix is not a square matrix!')
        return

    # 収束させるために固有値に微丈量を足す
    mu = lamb + 1e-5
    L, U = get_LU(A - mu * np.identity(n))
    x = np.ones(n)
    for k in range(k_max):
        # x_(k+1)を求めて正規化する
        next_x = calc_forward_backward_by_LU(L, U, x)
        next_x /= np.linalg.norm(next_x, ord=2)

        # 収束判定　固有ベクトルが符号違いのものに収束する可能性があるため
        if min(np.linalg.norm(next_x - x, ord=2), np.linalg.norm(next_x + x, ord=2)) < EPS:
            print(k)
            break
        x = next_x

    return x

# 参考文献: https://en.wikipedia.org/wiki/Inverse_iteration#:~:text=In%20numerical%20analysis%2C%20inverse%20iteration,similar%20to%20the%20power%20method.