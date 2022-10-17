import copy
from asgmt1.mytyping.typing import VectorS, FunctionS, FunctionV

def diff(f: FunctionS, x: float, h: float) -> float:
    return ( f(x+h) - f(x-h) ) / (2 * h)

def partial_diff(f: FunctionV, x:VectorS, h: float, m: int) -> float: #differentiate f(x) by x[m]
    x_plus: VectorS = copy.copy(x)
    x_plus[m] += h
    x[m] -= h
    return ( f(x_plus) - f(x) ) / (2 * h)