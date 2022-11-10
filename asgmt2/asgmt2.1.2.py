import numpy as np
from function.DLU_decomposition import get_DLU
from const_value import A
from function.calc_mat import calc_mat
from function.inverse_mat import get_inverse_matrix
from function.LU_decomposition import get_LU

def main():
    D, L, U = get_DLU(A)

    inv_arr1 = get_inverse_matrix(A)

    print(calc_mat(inv_arr1, A))

if __name__ == '__main__':
    main()