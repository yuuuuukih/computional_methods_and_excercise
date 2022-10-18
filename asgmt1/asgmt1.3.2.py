import numpy as np
from mytyping.typing import VectorS, VectorF, MatrixS, TrueSolDict
from function.newton_mutidim import newton_multidim
from typing import Final


def f1(vec_x: VectorS) -> float:
    x1, x2 = vec_x
    return x1**3 - 3 * x1 * x2**2 - 1

def f2(vec_x: VectorS) -> float:
    x1, x2 = vec_x
    return 3 * x1**2 * x2 - x2**3

def calc_distance(P: VectorS, Q: VectorS) -> float:
    dist_squared: float = 0
    for i in range(len(P)):
        dist_squared += (P[i] - Q[i])**2
    return np.sqrt(dist_squared)

def main():
    vec_f: VectorF = [f1, f2]
    vec_x0s: MatrixS = []
    NUMBER_OF_1D_PARTITIONS: Final[int] = 5 #1次元の分割数を定義

    #初期値ベクトルのリストを、縦横[-2, 2]かつNUMBER_OF_1D_PARTITIONSで分割
    for i in range(NUMBER_OF_1D_PARTITIONS):
        x = np.linspace(-2, 2, NUMBER_OF_1D_PARTITIONS)
        for j in range(NUMBER_OF_1D_PARTITIONS):
            y = np.linspace(-2, 2, NUMBER_OF_1D_PARTITIONS)
            vec_x0s.append([x[i], y[j]])
    #初期値が[0, 0]のときは計算不可なので取り除く
    vec_x0s = [vec_x0 for vec_x0 in vec_x0s if vec_x0 != [0, 0]]

    #それぞれの初期値に対する数値解をvec_solsに保尊
    vec_sols: MatrixS = []
    for vec_x0 in vec_x0s:
        vec_sols.append(newton_multidim(vec_f, 100, vec_x0)['sol'])

    print(vec_sols)
    TRUE_SOLS: Final[list[TrueSolDict]] = [
        {'label': '(1, 0)', 'true_sol': [1, 0]},
        {'label': '(-1/2, √3/2)', 'true_sol': [-1/2, np.sqrt(3)/2]},
        {'label': '(-1/2, -√3/2)', 'true_sol': [-1/2, -np.sqrt(3)/2]}
    ]

    return 0

if __name__ == '__main__':
    main()