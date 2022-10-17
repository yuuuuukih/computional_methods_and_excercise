from asgmt1.function.calcMV4 import calcMV4
from asgmt1.mytyping.typing import VectorS

def vvecGenerate(n0: float, n1: float, n2: float) -> VectorS:
    v0 = -n0*n1*n2
    v1 = n0*n1+n1*n2+n2*n0
    v2 = -n0-n1-n2
    v3 = 1

    return [v0, v1, v2, v3]

def main():
    x0 = 1
    x1 = 4/3
    x2 = 5/3
    x3 = 2

    vmat = [[1, x0, x0**2, x0**3],
            [1, x1, x1**2, x1**3],
            [1, x2, x2**2, x2**3],
            [1, x3, x3**2, x3**3]]

    print("f0:" + str(calcMV4(vmat, vvecGenerate(x1, x2, x3))))
    print("f1:" + str(calcMV4(vmat, vvecGenerate(x0, x2, x3))))
    print("f2:" + str(calcMV4(vmat, vvecGenerate(x1, x0, x3))))
    print("f3:" + str(calcMV4(vmat, vvecGenerate(x1, x2, x0))))


if __name__ == '__main__':
    main()