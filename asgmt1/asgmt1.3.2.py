import numpy as np
import pandas as pd
from mytyping.typing import VectorS, VectorF, MatrixS
from function.newton_mutidim import newton_multidim


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
    squared_number_of_divisions: int = 5
    for i in range(squared_number_of_divisions):
        x = np.linspace(-2, 2, squared_number_of_divisions)
        for j in range(squared_number_of_divisions):
            y = np.linspace(-2, 2, squared_number_of_divisions)
            vec_x0s.append([x[i], y[j]])

    ans: VectorS = []
    for vec_x0 in vec_x0s:
        ans.append(newton_multidim(vec_f, 100, vec_x0)['sol'])

    print(ans)
    return 0

if __name__ == '__main__':
    main()