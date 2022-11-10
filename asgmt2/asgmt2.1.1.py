from const_value import A
from function.LU_decomposition import get_LU

def main():
    L, U = get_LU(A)
    print(L)
    print(U)

if __name__ == '__main__':
    main()