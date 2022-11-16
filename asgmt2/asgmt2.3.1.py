import numpy as np
from function.QR_method import get_eigen_value_by_QR
from const_value import A
from function.inverse_iteration import calc_inverse_iteration

# QR法で固有値を求めて、逆反復法で固有ベクトルを求める
def main():
    eigenval = get_eigen_value_by_QR(A)
    eigenval_max = max(eigenval)
    eigenval_min = min(eigenval)
    eigenvec_max = calc_inverse_iteration(A, eigenval_max)
    eigenvec_min = calc_inverse_iteration(A, eigenval_min)

    print(f'eigenval_max: {eigenval_max}\n'
          f'eigenvec_max: {eigenvec_max}\n'
          f'eigenval_min: {eigenval_min}\n'
          f'eigenval_min: {eigenvec_min}')

if __name__ == '__main__':
    main()