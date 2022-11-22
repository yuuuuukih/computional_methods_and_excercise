import numpy as np
from function.QR_method import get_eigen_value_by_QR

# Aを下三角行列にする
def get_tril(A):
    n = len(A)
    L = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1):
            L[i][j] = A[i][j]
    return L

# n次元の対称行列を生成
def get_symmetric_matrix(n):
    A = np.random.randn(n, n)
    A = get_tril(A)
    A += A.T
    return A

# QR法で固有値を求めて、条件数を求める
def main():
    # 対称行列を生成
    dim = 9
    A = get_symmetric_matrix(dim)
    print(f'A: {A}')

    eigenval = get_eigen_value_by_QR(A)
    print(f'eigenval: {eigenval}')
    abs_eigenval = np.abs(eigenval)

    cond_num = max(abs_eigenval) / min(abs_eigenval)
    print(f'condition number: {cond_num}')

if __name__ == '__main__':
    main()