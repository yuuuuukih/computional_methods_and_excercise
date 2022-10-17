import numpy as np
from mytyping.typing import VectorS
from function.newton_mutidim import newton_multidim


def f1(vec_x: VectorS) -> float:
    x1, x2 = vec_x
    return x1**3 - 3 * x1 * x2**2 - 1

def f2(vec_x: VectorS) -> float:
    x1, x2 = vec_x
    return 3 * x1**2 * x2 - x2**3

def main():
    # solve_by_gaussian_elimination([[2,3,-1],[-2,1,1],[1,1,-1]], [-3,2,-2])
    vec_f = [f1, f2]
    vec_x0 = [np.sqrt(2), np.sqrt(2)]
    newton_multidim(vec_f, 100, vec_x0)


if __name__ == '__main__':
    main()