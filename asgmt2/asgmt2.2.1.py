import numpy as np
from const_value import A, b1, b2, b3, alpha1, alpha2, alpha3
from function.LU_decomposition import get_LU
from function.substitution_method import calc_forward_backward_by_LU

def main():
    L, U = get_LU(A)
    x1 = calc_forward_backward_by_LU(L, U, b1)
    x2 = calc_forward_backward_by_LU(L, U, b2)
    x3 = calc_forward_backward_by_LU(L, U, b3)
    print(f'x: {x1}\n'
          f'x2: {x2}\n'
          f'x3: {x3}\n'
          f'(x1-alpha1)^2: {np.linalg.norm(x1 - alpha1, ord=2) ** 2}\n'
          f'(x2-alpha2)^2: {np.linalg.norm(x2-alpha2, ord=2)**2}\n'
          f'(x3-alpha3)^2: {np.linalg.norm(x3-alpha3, ord=2)**2}')

if __name__ == '__main__':
    main()