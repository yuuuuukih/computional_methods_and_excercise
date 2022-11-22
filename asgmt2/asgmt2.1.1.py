import numpy as np
from const_value import A, b1, alpha1
from function.LU_decomposition import get_LU
from function.substitution_method import calc_forward_backward_by_LU
import sys

def main():
    L, U = get_LU(A)
    x = calc_forward_backward_by_LU(L, U, b1)
    print(f'x: {x}')
    print(f'(x-alpha1)^2: {np.linalg.norm(x-alpha1, ord=2)**2}')

    print(f'machine epsilon: {sys.float_info.epsilon}')

if __name__ == '__main__':
    main()