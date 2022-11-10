import numpy as np
from const_value import A, b1, alpha1
from function.LU_decomposition import get_LU
from function.substitution_method import calc_forward, calc_backward

def main():
    L, U = get_LU(A)
    y = calc_forward(L, b1)
    x = calc_backward(U, y)
    print(f'x: {x}')
    print(f'(x-alpha1)^2: {np.linalg.norm(x-alpha1, ord=2)**2}')

if __name__ == '__main__':
    main()