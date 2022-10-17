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

class OutputFunc(TypedDict):
    sol: float
    err: VectorS
    cnt: int