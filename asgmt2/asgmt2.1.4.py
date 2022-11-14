import numpy as np
from const_value import A, b1
from function.modified_cholosky_decomposition import get_U_by_LD
from function.ICCG_method import calc_ICCG_method

def main():
    x = calc_ICCG_method(A, b1)
    print(x[-1])

if __name__ == '__main__':
    main()