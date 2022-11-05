import copy
from asgmt1.mytyping.typing import VectorS, FunctionS, FunctionV

# 微分の計算では、誤差が最も小さくなる中心差分法を用いた

# 1変数関数の1階微分を行う
def diff(f: FunctionS, x: float, h: float) -> float:
    return ( f(x+h) - f(x-h) ) / (2 * h)

# 多変数関数の偏微分を行う
def partial_diff(f: FunctionV, x:VectorS, h: float, m: int) -> float: #differentiate f(x) by x[m]
    x_plus: VectorS = copy.copy(x)
    x_plus[m] += h
    x[m] -= h
    return ( f(x_plus) - f(x) ) / (2 * h)