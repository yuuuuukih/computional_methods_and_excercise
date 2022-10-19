from typing import TypedDict

#function(scaler)
FunctionS = any

#function(vector)
FunctionV = any

#vector of scaler (flaot)
VectorS = list[float]
MatrixS = list[VectorS]

#vector of function
VectorF = list[any]
MatrixF = list[VectorF]

#output of algorithm
class _OutputFuncRequired(TypedDict):
    sol: float | VectorS
    cnt: int

class _OutputFuncOptional(TypedDict, total=False):
    err: VectorS

class OutputFunc(_OutputFuncRequired, _OutputFuncOptional):
    pass

#true solution dictionary
class TrueSolDict(TypedDict):
    label: str
    true_sol: VectorS