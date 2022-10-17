from .differentiation import partial_diff
from asgmt1.mytyping.typing import VectorS, MatrixS, VectorF

def jacobian(vec_x: VectorS,vec_f: VectorF) -> MatrixS:
    jac: MatrixS = []
    for f in vec_f:
        jac.append([partial_diff(f, vec_x, 1e-5, m) for m in range(len(vec_x))])

    return jac