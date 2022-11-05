from typing import Final
from .differentiation import diff
from asgmt1.mytyping.typing import FunctionS, VectorS, OutputFunc


def newton(f: FunctionS, k_max: int, x_0: float, eps: float) -> OutputFunc:
    k: int = 0
    x: VectorS = [x_0]
    TRUE_VALUE: Final[float] = 1.4142135623730954
    err: VectorS = []
    while k < k_max:
        x.append(x[k] - f(x[k]) / diff(f, x[k], 0.001))

        if abs(x[k+1] - x[k]) > eps:
            err.append(abs(x[k+1] - TRUE_VALUE))
            k += 1
        else:
            break

    output: OutputFunc = {'sol': x[k], 'err': err, 'cnt': len(x)-1}

    return output