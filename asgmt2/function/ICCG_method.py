import numpy as np
from .modified_cholosky_decomposition import get_U_by_LD
from .check_matrix import Ab_error_check
from .calc_mat_vec import calc_mat_vec
from .inverse_mat import get_inverse_matrix
from .substitution_method import calc_forward_backward_by_LU
from tqdm import tqdm
from asgmt2.decorator.TimeMeasurement import print_proc_time

@print_proc_time
def calc_ICCG_method(A, b, EPS=1e-10):
    # A,b次元チェック
    Ab_error_check(A, b)

    inv_A = get_inverse_matrix(A)

    n = len(A)
    U = get_U_by_LD(A)
    x = np.zeros(n).reshape(1, n)
    r = np.array([b - calc_mat_vec(A, x[0])]).reshape(1, n)

    p0 = calc_forward_backward_by_LU(U.T, U, r[0])
    p = np.array([p0]).reshape(1, n)
    r_tilde = np.array([p0]).reshape(1, n)

    # 修正係数 modification factor
    mf_alpha = np.array([])
    mf_beta = np.array([])

    for k in tqdm(range(n)):
        y = calc_mat_vec(A, p[k])
        new_alpha = np.dot(r[k], calc_mat_vec(inv_A, r[k])) / np.dot(p[k], y)
        mf_alpha = np.append(mf_alpha, new_alpha)
        x = np.append(x, x[k] + mf_alpha[k] * p[k]).reshape(k+2, n)
        r = np.append(r, r[k] - mf_alpha[k] * y).reshape(k+2, n)

        if np.linalg.norm(r[-1], ord=2) < EPS:
            break

        new_r_tilde = calc_forward_backward_by_LU(U.T, U, r[k+1])
        r_tilde = np.append(r_tilde, new_r_tilde).reshape(k+2, n)

        new_beta = np.dot(r[k+1], r_tilde[k+1]) / np.dot(r[k], r_tilde[k])
        mf_beta = np.append(mf_beta, new_beta)

        new_p = r_tilde[k+1] + mf_beta[k] * p[k]
        p = np.append(p, new_p).reshape(k+2, n)

        k += 1

    return x


# 参考文献: http://www.slis.tsukuba.ac.jp/~fujisawa.makoto.fu/cgi-bin/wiki/index.php?%C1%B0%BD%E8%CD%FD%C9%D5%A4%AD%B6%A6%CC%F2%B8%FB%C7%DB%CB%A1