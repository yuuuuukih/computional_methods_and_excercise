import numpy as np
from tqdm import tqdm
from .DLU_decomposition import get_DLU
from .calc_mat import calc_mat
from .calc_mat_vec import calc_mat_vec
from .inverse_mat import get_inverse_matrix
from .residual_norm import get_residual_norm
from .check_matrix import Ab_error_check

# 反復法で解く
METHODS = ['jacobi', 'gauss_seidel', 'sor']
def calc_iterative_method(A, b, alpha=0, method=METHODS[0], omega=1.9, EPS=1e-10, k_max=10000, new_ver=False):
    # methodチェック
    if not(method in METHODS):
        print('Method Error!')
        return
    if not(0 < omega < 2):
        print('Omega Error!')
        return

    # A,bの次元チェック
    Ab_error_check(A, b)

    # M,N生成
    D, L, U = get_DLU(A)
    M = D if method == 'jacobi' else D + L if method == 'gauss_seidel' else (D + omega * L) / omega if method == 'sor' else np.array([])
    N = M - A

    n = len(A)
    B = calc_mat(get_inverse_matrix(M), N)
    c = calc_mat_vec(get_inverse_matrix(M), b)

    x = np.zeros(n).reshape(1, n)
    r = np.array([np.linalg.norm(b - calc_mat_vec(A, x[0]), ord=2)])

    for k in tqdm(range(k_max)):
        x_next = calc_mat_vec(B, x[k]) + c
        x = np.append(x, x_next).reshape(k+2, n)

        r_next = np.linalg.norm(b - calc_mat_vec(A, x[-1]), ord=2)
        r = np.append(r, r_next)

        if not(new_ver) and r[-1] < EPS or new_ver and r[-1] / np.linalg.norm(b, ord=2) < EPS:
            break

    e = get_residual_norm(x, alpha)

    output = {
        'sol': x,
        'r': r,
        'e': e
    }

    return output

