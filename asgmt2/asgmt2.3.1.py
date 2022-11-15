import numpy as np
from function.QR_method import get_eigen_value_by_QR
from function.QR_decomposition import get_QR
from const_value import A

def main():
    # A = np.array([[1., 5., 4.],
    #               [2., 4., -7.],
    #               [2., 7., 14.]])

    # A = np.array([[6., -3., 5.], [-1., 4., -5.], [-3., 3., -4.]])
    # Q, R = get_QR(A)
    ev = get_eigen_value_by_QR(A)
    print(ev)


if __name__ == '__main__':
    main()