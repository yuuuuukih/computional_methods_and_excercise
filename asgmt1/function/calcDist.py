import numpy as np
from asgmt1.mytyping.typing import VectorS

#PとQのユークリッド距離を求める
def calc_distance(P: VectorS, Q: VectorS) -> float:
    dist_squared: float = 0
    for i in range(len(P)):
        dist_squared += (P[i] - Q[i])**2
    return np.sqrt(dist_squared)