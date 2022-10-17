from asgmt1.mytyping.typing import VectorS, MatrixS

def calcMV4(mat: MatrixS, vec: VectorS) -> VectorS:
    ans: VectorS = [0] * len(vec)
    for i in range(len(vec)):
        ans[i] = sum([mat[i][j] * vec[j] for j in range(len(vec))])
    return ans