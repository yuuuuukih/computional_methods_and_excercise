import numpy as np

# 残差ノルムeを計算
def get_residual_norm(vecs, TRUE_VECTOR):
    e = np.array([])
    for vec in vecs:
        e = np.append(e, np.linalg.norm((TRUE_VECTOR - vec), ord=2))
    return e