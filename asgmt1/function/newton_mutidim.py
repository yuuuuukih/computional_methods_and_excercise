from .jacobian import jacobian
from asgmt1.mytyping.typing import VectorS, MatrixS, VectorF
from .GaussianElimination import solve_by_gaussian_elimination

def newton_multidim(vec_f: VectorF, k_max: int, vec_x0: VectorS) -> None:
    vec_x: MatrixS = [vec_x0] #xkを保存
    vec_delta_x: MatrixS = [] #delta_xkを保存
    vec_f_x: MatrixS = [] #vec_fにvec_xkを代入したもの(vec_f(vec_xk))を保存
    k: int = 0
    jacs: list[MatrixS] = [] #J(xk)を保存

    while k < k_max:
        #jacobian(vec_x[k], vec_f) * vec_delta_x[k] = -vec_f
        jacs.append(jacobian(vec_x[k], vec_f)) #jac[k] = J(vec_xk)
        vec_f_x.append([f(vec_x[k]) for f in vec_f]) #vec_f_x[k] = vec_f(vec_xk)
        vec_delta_x.append(solve_by_gaussian_elimination(jacs[k], [-1 * el for el in vec_f_x[k]])) #solve_by_gaussian_eliminationの第2引数は、vec_f_x[k]の各要素をそれぞれ-1倍したものをリストに格納
        vec_x.append([xk + delta_xk for (xk, delta_xk) in zip(vec_x[k], vec_delta_x[k])]) #x(k+1) = xk + delta_xk

        k += 1

    print(vec_x[k])