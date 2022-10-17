from typing import Final
from asgmt1.mytyping.typing import FunctionS, VectorS, OutputFunc

def dichotomy(f: FunctionS, x1_0: float, x2_0: float ,eps: float) -> OutputFunc:
    x1: VectorS = [x1_0]
    x2: VectorS = [x2_0]
    x_mid: VectorS = []
    k: int = 0
    TRUE_VALUE: Final[float] = 1.4142135623730954
    err: VectorS = []
    while abs(x1[k] - x2[k]) >= eps:
        x_mid.append((x1[k] + x2[k]) / 2)

        if f(x_mid[k]) * f(x2[k]) < 0:
            x1.append(x_mid[k])
            x2.append(x2[k])
        else:
            x2.append(x_mid[k])
            x1.append(x1[k])

        err.append(abs(x_mid[k] - TRUE_VALUE))
        k += 1

    # print("dichotomy: ", x_mid[k - 1])
    # print("dichotomy: ", cnt)
    output: OutputFunc = {'sol': x_mid[k - 1], 'err': err, 'cnt': len(x_mid)}

    return output