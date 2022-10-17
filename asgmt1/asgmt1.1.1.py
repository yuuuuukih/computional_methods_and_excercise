from function.calcMV4 import calcMV4
from asgmt1.mytyping.typing import VectorS, MatrixS

def main():
    x0 = 1
    x1 = 4/3
    x2 = 5/3
    x3 = 2

    vmat: MatrixS = [[1, x0, x0**2, x0**3],
                     [1, x1, x1**2, x1**3],
                     [1, x2, x2**2, x2**3],
                     [1, x3, x3**2, x3**3]]

    vec: VectorS = [1, 1, 1, 1]

    print(calcMV4(vmat, vec))


if __name__ == '__main__':
    main()