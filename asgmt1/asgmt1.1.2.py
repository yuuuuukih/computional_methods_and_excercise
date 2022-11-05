from asgmt1.function.calcMV4 import calcMV4
from asgmt1.mytyping.typing import VectorS
import numpy as np

# (v0, v1, v2, v3)^Tを生成
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

    # 計算結果を表示
    print(f'coef_f0: {vvecGenerate(x1, x2, x3)}\n'
          f'coef_f1: {vvecGenerate(x0, x2, x3)}\n'
          f'coef_f2: {vvecGenerate(x1, x0, x3)}\n'
          f'coef_f3: {vvecGenerate(x1, x2, x0)}\n\n'
          f'A*f0: {calcMV4(vmat, vvecGenerate(x1, x2, x3))}\n'
          f'A*f1: {calcMV4(vmat, vvecGenerate(x0, x2, x3))}\n'
          f'A:f2: {calcMV4(vmat, vvecGenerate(x1, x0, x3))}\n'
          f'A*f3: {calcMV4(vmat, vvecGenerate(x1, x2, x0))}\n')

    # A*[f0, f1, f2, f3]が単位行列になるように対応する成分で除算
    #nmdはnormalizedの略称
    nmd_coef_f0 = np.array(vvecGenerate(x1, x2, x3)) / calcMV4(vmat, vvecGenerate(x1, x2, x3))[0]
    nmd_coef_f1 = np.array(vvecGenerate(x0, x2, x3)) / calcMV4(vmat, vvecGenerate(x0, x2, x3))[1]
    nmd_coef_f2 = np.array(vvecGenerate(x1, x0, x3)) / calcMV4(vmat, vvecGenerate(x1, x0, x3))[2]
    nmd_coef_f3 = np.array(vvecGenerate(x1, x2, x0)) / calcMV4(vmat, vvecGenerate(x1, x2, x0))[3]

    vmat_inv = np.array([nmd_coef_f0, nmd_coef_f1, nmd_coef_f2, nmd_coef_f3]).T
    print(vmat_inv)


if __name__ == '__main__':
    main()