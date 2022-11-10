import numpy as np
from DLU_decomposition import get_DLU

def calc_iterative_method(A, b, method='jacobi', omega=1.9):
    # methodチェック
    if method != 'jacobi' or 'gauss_seidel' or 'sor':
        print('Method Error!')
        return
    if not(0 < omega < 2):
        print('Omega Error!')
        return

    # M,N生成
    D, L, U = get_DLU(A)
    M = D if method == 'jacobi' else D + L if method == 'gauss_seidel' else (D + omega * L) / omega if method == 'sor' else np.array([])
    N = A - M

    n = len(A)
    x = np.full(n, np.random.randn())

